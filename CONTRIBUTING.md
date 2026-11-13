# Contributing

## Branches

| Branch | Purpose | Who pushes to it |
|---|---|---|
| `main` | Released code. Always works. | Nobody. Only a pull request from `dev`. |
| `dev` | Finished work that is waiting for the next release. | Nobody. Only pull requests from feature branches. |
| `<name>/<task>` | One task by one person, for example `joyce/median`. | Only its owner. |

`main` and `dev` are protected. A direct `git push` to them fails:

```
remote: error: GH013: Repository rule violations found for refs/heads/dev.
```

## Workflow for one task

1. Take an issue on GitHub. Assign it to yourself.
2. Start from the newest `dev`:

   ```bash
   git switch dev
   git pull
   git switch -c joyce/median
   ```

3. **Red:** write a test for the new behaviour in `tests/`. Run `pytest`. The test must fail.
4. Commit the test and push. Open a **draft** pull request into `dev`. CI is red. This is correct.
5. **Green:** write the smallest code that makes the test pass. Run `pytest`.
6. **Refactor:** clean up the code. The tests must stay green.
7. Run all checks (see the README). Commit and push. CI turns green.
8. Mark the pull request as **Ready for review**. Ask a teammate to review it.
9. Fix review comments with new commits on the same branch.
10. When CI is green and a teammate approves, click **Squash and merge**.
11. Delete the branch. Start the next task from step 2.

## Your branch is out of date with `dev`

A teammate merged into `dev` after you made your branch. GitHub says "This branch is out of date with the base branch". Rebase your branch onto the new `dev`:

```bash
git fetch origin
git rebase origin/dev
```

If there is a conflict: fix the file, then `git add <file>` and `git rebase --continue`. To stop and go back: `git rebase --abort`.

Then push. A rebase rewrites your commits, so a normal push fails. Use:

```bash
git push --force-with-lease
```

Use `--force-with-lease` **only on your own branch**. Never on `dev` or `main`.

## Release: `dev` into `main`

1. Open a pull request from `dev` into `main`.
2. CI runs again. A teammate approves.
3. Click **Create a merge commit**. Do not squash or rebase this pull request. Then `main` and `dev` keep the same commits.
4. The `Build` workflow runs on `main` and saves the package as an artifact.

## Code style

- Every public function has a docstring and tests.
- Add each new public function to `src/tinystats/__init__.py`.
- `ruff format .` formats the code for you.
