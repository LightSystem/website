---
name: pr-preparation
description: Prepares the latest commit for a Pull Request by renaming WIP commits and adding a summary of changes. Use this when the user asks to prepare, finalize, or "wrap up" a PR or commit.
---

# PR Preparation

This skill streamlines the process of finalizing work before a Pull Request.

## Workflow

When asked to prepare the latest commit for a PR:

1. **Rename WIP Commit**: Identify the latest local commit. If it is a "WIP" (Work In Progress) commit, rename it to a
   concise `<one-line summary>` that describes the overall change.
2. **Add Summary**: Add a new line to the commit message with short phrases summarizing the main changes included in
   that PR.

See examples in the commit history.
