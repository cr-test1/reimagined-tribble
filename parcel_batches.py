def dispatch_batches(parcel_count: int, batch_capacity: int) -> int:
    """Count the batches needed to dispatch all parcels, including a partial batch."""
    if parcel_count < 0 or batch_capacity < 1:
        raise ValueError("Expected a nonnegative parcel count and a positive capacity")
    if parcel_count == 0:
        return 0
    return parcel_count // batch_capacity + 1
