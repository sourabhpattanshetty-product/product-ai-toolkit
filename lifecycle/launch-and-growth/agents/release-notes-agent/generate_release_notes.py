#!/usr/bin/env python3
"""
Release Notes Agent - reference implementation.

Reads commit history from a local git repo between two refs and produces
customer-facing release notes grouped by conventional-commit type. This is
the one agent in this toolkit that runs with zero external credentials -
it only needs `git` and a repo to read.

Usage:
    python generate_release_notes.py [--repo PATH] [--from REF] [--to REF]

If --from is omitted, it defaults to the most recent tag (or the first
commit, if there are no tags). If --to is omitted, it defaults to HEAD.
"""

import argparse
import re
import subprocess
import sys
from collections import defaultdict

TYPE_LABELS = {
    "feat": "Features",
    "fix": "Fixes",
    "perf": "Performance",
    "docs": "Documentation",
    "refactor": "Internal changes",
    "chore": "Chores",
    "test": "Tests",
}

CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(?P<type>feat|fix|perf|docs|refactor|chore|test)(\((?P<scope>[^)]+)\))?!?:\s*(?P<subject>.+)$"
)


def run_git(args, repo_path):
    result = subprocess.run(
        ["git", "-C", repo_path] + args,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def most_recent_tag(repo_path):
    try:
        return run_git(["describe", "--tags", "--abbrev=0"], repo_path)
    except subprocess.CalledProcessError:
        return None


def get_commits(repo_path, from_ref, to_ref):
    range_spec = f"{from_ref}..{to_ref}" if from_ref else to_ref
    log = run_git(
        ["log", range_spec, "--format=%H%x01%s%x01%an"],
        repo_path,
    )
    commits = []
    for line in log.splitlines():
        if not line.strip():
            continue
        sha, subject, author = line.split("\x01")
        commits.append({"sha": sha[:7], "subject": subject, "author": author})
    return commits


def classify(commits):
    grouped = defaultdict(list)
    uncategorized = []
    for commit in commits:
        match = CONVENTIONAL_COMMIT_RE.match(commit["subject"])
        if match:
            ctype = match.group("type")
            scope = match.group("scope")
            subject = match.group("subject")
            label = f"**{scope}:** {subject}" if scope else subject
            grouped[ctype].append({**commit, "clean_subject": label})
        else:
            uncategorized.append(commit)
    return grouped, uncategorized


def render_markdown(grouped, uncategorized, from_ref, to_ref):
    lines = [f"# Release Notes: {from_ref or 'start'} -> {to_ref}", ""]
    for ctype, label in TYPE_LABELS.items():
        items = grouped.get(ctype)
        if not items:
            continue
        lines.append(f"## {label}")
        for item in items:
            lines.append(f"- {item['clean_subject']} ({item['sha']})")
        lines.append("")
    if uncategorized:
        lines.append("## Other changes")
        lines.append(
            "_These commits don't follow the `type: subject` convention "
            "and are listed as-is - consider tightening commit message "
            "conventions to improve future release notes._"
        )
        for item in uncategorized:
            lines.append(f"- {item['subject']} ({item['sha']})")
        lines.append("")
    if not grouped and not uncategorized:
        lines.append("_No commits found in this range._")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path to the git repo")
    parser.add_argument("--from", dest="from_ref", default=None, help="Starting ref (exclusive)")
    parser.add_argument("--to", dest="to_ref", default="HEAD", help="Ending ref (inclusive)")
    args = parser.parse_args()

    # If no --from is given, use the most recent tag; if there is no tag
    # either, fall back to showing full history rather than guessing a range.
    from_ref = args.from_ref or most_recent_tag(args.repo)

    try:
        commits = get_commits(args.repo, from_ref, args.to_ref)
    except subprocess.CalledProcessError as exc:
        print(f"git command failed: {exc.stderr}", file=sys.stderr)
        sys.exit(1)

    grouped, uncategorized = classify(commits)
    print(render_markdown(grouped, uncategorized, from_ref, args.to_ref))


if __name__ == "__main__":
    main()
