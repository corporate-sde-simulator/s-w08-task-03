# PR Review - Incident ticket auto-classifier (by Vikram Singh)

## Reviewer: Pooja Reddy
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `ticketClassifier.py`

> **Bug #1:** Keyword scoring counts substring matches so error also matches terror and mirror
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `keywordMatcher.py`

> **Bug #2:** Priority assignment uses first matching rule instead of highest severity and P1 issues classified as P3
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Vikram Singh**
> Acknowledged. I have documented the issues for whoever picks this up.
