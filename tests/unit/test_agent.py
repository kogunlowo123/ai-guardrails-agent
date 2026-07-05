"""AI Guardrails Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_validate_input():
    """Test Validate user input against guardrail rules before LLM processing."""
    tools = AgentTools()
    result = await tools.validate_input(input_text="test", rules="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_filter_output():
    """Test Filter LLM output for policy violations before returning to user."""
    tools = AgentTools()
    result = await tools.filter_output(output_text="test", policies="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_pii():
    """Test Detect and classify PII in text (names, emails, SSN, etc.)."""
    tools = AgentTools()
    result = await tools.detect_pii(text="test", pii_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_screen_toxicity():
    """Test Screen text for toxic, harmful, or inappropriate content."""
    tools = AgentTools()
    result = await tools.screen_toxicity(text="test", threshold="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ai_guardrails_agent_agent import AiGuardrailsAgentAgent
    agent = AiGuardrailsAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
