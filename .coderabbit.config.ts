import { defineConfig, mergeConfig } from "@coderabbitai/config";
import reviewSettings from "./config/reviews.ts";

export default defineConfig((ctx) =>
  mergeConfig(
    { version: 3, inheritance: false },
    reviewSettings,
    { fun: { art: ctx.invocation.source === "review" } },
  ),
);
