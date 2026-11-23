import type { CodeRabbitConfigV3Fragment } from "@coderabbitai/config";

const reviewSettings: CodeRabbitConfigV3Fragment = {
  reviews: {
    behavior: { profile: "assertive" },
    auto_review: {
      enabled: true,
      base_branches: ["^hasit/v3-typescript-optin-base-20261123$"],
    },
    output: { summary: { placement: "walkthrough" } },
  },
};

export default reviewSettings;
