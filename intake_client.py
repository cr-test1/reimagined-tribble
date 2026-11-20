"""Send a caller-provided parcel to the shared intake library."""

from parcel_intake import accept_parcel


def submit_parcel(parcel_id: str, route_tag: str):
    return accept_parcel({"id": parcel_id, "route_tag": route_tag})
