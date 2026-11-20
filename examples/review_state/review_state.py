"""Classify a completed review against the current pull request head."""


def review_state(head_sha, status, reviewed_sha):
    if status != "completed" or not head_sha or not reviewed_sha:
        return "unknown"
    if head_sha == reviewed_sha:
        return "current"
    return "stale"
