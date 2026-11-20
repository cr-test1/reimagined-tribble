"""Count changed files by their final, case-normalized extension."""

from collections import Counter
from pathlib import PurePosixPath


def count_file_kinds(paths):
    counts = Counter()
    for path in paths:
        suffix = PurePosixPath(path).suffix.lower()
        counts[suffix or "(no extension)"] += 1
    return dict(sorted(counts.items()))
