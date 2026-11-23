import type { CodeRabbitConfigV3Fragment } from "@coderabbitai/config";

const reviewSettings: CodeRabbitConfigV3Fragment = {
  reviews: {
    behavior: { profile: "assertive" },
    auto_review: { enabled: true },
    output: { summary: { placement: "walkthrough" } },
  },
};

export default reviewSettings;
