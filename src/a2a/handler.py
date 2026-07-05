"""AI Guardrails Agent - A2A Handler."""

import structlog

logger = structlog.get_logger(__name__)


class A2AHandler:
    """Agent-to-agent communication handler for AI Guardrails Agent."""

    def __init__(self):
        logger.info("a2a_handler_initialized")
