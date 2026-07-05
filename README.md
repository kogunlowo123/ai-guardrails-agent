# AI Guardrails Agent

[![CI](https://github.com/kogunlowo123/ai-guardrails-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ai-guardrails-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI safety guardrails agent that implements input/output validation, content filtering, topic restriction, PII detection, toxicity screening, and jailbreak prevention for production LLM applications.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `validate_input` | Validate user input against guardrail rules before LLM processing |
| `filter_output` | Filter LLM output for policy violations before returning to user |
| `detect_pii` | Detect and classify PII in text (names, emails, SSN, etc.) |
| `screen_toxicity` | Screen text for toxic, harmful, or inappropriate content |
| `detect_jailbreak` | Detect prompt injection and jailbreak attempts |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/guardrails/validate-input` | Validate input |
| `POST` | `/api/v1/guardrails/filter-output` | Filter output |
| `POST` | `/api/v1/guardrails/detect-pii` | Detect PII |
| `POST` | `/api/v1/guardrails/screen-toxicity` | Screen toxicity |
| `POST` | `/api/v1/guardrails/detect-jailbreak` | Detect jailbreak |

## Features

- Input Validation
- Output Filtering
- Pii Detection
- Toxicity Screening
- Jailbreak Prevention

## Integrations

- Guardrails Ai
- Nemo Guardrails
- Presidio
- Openai Moderation
- Perspective Api

## Architecture

```
ai-guardrails-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ai_guardrails_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Guardrails AI + NeMo Guardrails + Custom Validators**

---

Built as part of the Enterprise AI Agent Platform.
