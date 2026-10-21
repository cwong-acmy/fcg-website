# State Log

## 2026-09-06 — Six existing worktree links repaired

- Native `git worktree repair` restored forward/backlinks for about, advisory-implementation, agreeease, atlas, corporate-booking-tool and whitelabel. All six branch heads and index hashes remained identical; all recorded working-file hashes matched before/after.
- No source, assets, branch history, remote, folder locations or deployment changed. Exact pointer backups and verification: `../00.Project Index/workflow-cleanup-2026-09-06/git-repair-result.json`.

### Decisions

- Preserve these separate branch workspaces in place; no move or consolidation is necessary to restore their history access.

## 2026-08-02 — Folder cleanup

- Flattened each single-child `outputs/copy-feedback/` wrapper to `copy-feedback/` across the main worktree and six page worktrees; updated all seven review-build scripts to write to the new path.
- Flattened the dated working web-copy archive without changing its files.

## Current Status
This is the "codex/drafts" worktree of the fcg-website repo — the main working copy of the FCG marketing site (root `index.html` + shared assets). Active as of last commit; not dormant.

## Latest Update
Date: 2026-07-10
What changed: Pruned an extracted design archive (chore commit), following a run of copy tweaks (dropped "in RMB" from nav payment teaser across all pages, updated payment page `<title>`) and a theme fix (stopped a global hero override from clobbering scoped page heroes), plus an earlier pass aligning all pages to the company deck and standardizing visuals.
Why it matters: Site-wide copy, theme, and visual consistency pass across the whole marketing site.

## Decisions
- —

## Blockers
- —

## Next Actions
- Resume by reading git log on this branch; last work was a cleanup/prune commit so check whether any further design-archive or theme follow-ups are pending.

## Note
This is a git worktree of cwong-acmy/fcg-website — never mv/merge/archive the folder; use git worktree commands. Backfilled 2026-07-11 by the Claude Loop Rollout; first stub.


## 2026-09-07 — Shared instruction cleanup

Aligned local-preview guidance with standing authorization for requested builds. Only instruction text changed; existing hooks, configuration, application code and unrelated edits were preserved. Exact before/after hashes and contextual diffs: `/Users/crystalwong/Desktop/Claude/03.Code Projects/00.Project Index/workflow-cleanup-2026-09-06/instructions-closeout-20260907/`. Static review only; no runtime, provider or deployment claim.

### Decisions

- A missing optional code map is not a startup blocker. Installation, hook replacement, publication and deletion retain their separate approval gates.
