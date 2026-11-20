"""Construct and submit a manifest to the intake library."""

from parcel_intake import validate_manifest


def submit_manifest(manifest_id: str):
    return validate_manifest({"id": manifest_id, "variant": "stable"})
