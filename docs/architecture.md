# AI Guardrails Agent Architecture

AI safety guardrails agent that implements input/output validation, content filtering, topic restriction, PII detection, toxicity screening, and jailbreak prevention for production LLM applications.

## Domain Tools

- **validate_input**: Validate user input against guardrail rules before LLM processing
- **filter_output**: Filter LLM output for policy violations before returning to user
- **detect_pii**: Detect and classify PII in text (names, emails, SSN, etc.)
- **screen_toxicity**: Screen text for toxic, harmful, or inappropriate content
- **detect_jailbreak**: Detect prompt injection and jailbreak attempts