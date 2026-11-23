"""Rack planning for the synthetic parcel scanner."""

PARCELS_PER_RACK = 8


def racks_needed(parcels: int) -> int:
    """Return the number of racks needed to hold all parcels."""
    if parcels < 0:
        raise ValueError("Parcel count cannot be negative")
    full_racks, remaining = divmod(parcels, PARCELS_PER_RACK)
    return full_racks + int(remaining > 0)
