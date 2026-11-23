import assert from "node:assert/strict";
import test from "node:test";
import { batchParcels } from "../src/parcel-batches.mjs";

test("keeps dispatch order and the partial final batch", () => {
  assert.deepEqual(batchParcels(["north", "east", "west"], 2), [
    ["north", "east"],
    ["west"],
  ]);
});

test("rejects a capacity that cannot advance the batch", () => {
  assert.throws(() => batchParcels(["north"], 0), RangeError);
});

test("rejects an individual parcel label instead of splitting its characters", () => {
  assert.throws(() => batchParcels("north", 2), TypeError);
});
