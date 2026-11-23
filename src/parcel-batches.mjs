/** Split parcels into loading batches without changing their dispatch order. */
export function batchParcels(parcels, capacity) {
  if (!Number.isSafeInteger(capacity) || capacity < 1) {
    throw new RangeError("Capacity must be a positive integer");
  }

  const batches = [];
  for (let start = 0; start < parcels.length; start += capacity) {
    batches.push(parcels.slice(start, start + capacity));
  }
  return batches;
}
