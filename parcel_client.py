"""Build the parcel request sent to the intake service."""


def build_parcel_request(parcel_id: str) -> dict[str, str]:
    if not parcel_id:
        raise ValueError("A parcel id is required")
    return {"id": parcel_id, "route_tag": "standard"}
