"""List the changed paths for which a caller has no review evidence."""


def uncovered_paths(changed_paths, reviewed_paths):
    """Return each unreviewed changed path once, in sorted order."""
    return sorted(set(changed_paths).difference(reviewed_paths))
