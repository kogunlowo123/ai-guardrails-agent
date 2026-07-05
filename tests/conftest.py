"""Test configuration for AI Guardrails Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ai-guardrails-agent", "category": "AI Engineering"}
