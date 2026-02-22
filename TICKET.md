# FINSERV-4255: Fix support ticket auto-classifier misrouting tickets

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 30 · **Story Points:** 5
**Reporter:** Anjali Nair (Support Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `support`, `classification`
**Task Type:** Bug Fix

---

## Description

The support ticket classifier uses keyword matching to route tickets to the right team. Two bugs are causing tickets to be sent to wrong teams. Bugs are marked with `# BUG:` comments.

## Acceptance Criteria

- [ ] Bug #1 fixed: Keyword matching is case-sensitive — "Payment" doesn't match "payment"
- [ ] Bug #2 fixed: Priority scoring uses wrong weights — low keywords score higher than critical
- [ ] All unit tests pass
