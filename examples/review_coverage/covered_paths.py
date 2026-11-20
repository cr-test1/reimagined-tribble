"""List the changed paths for which a caller has no review evidence."""


def uncovered_paths(changed_paths, reviewed_paths):
    return sorted(set(changed_paths).difference(reviewed_paths))
