
from .prompt import build_prompt
from ..config import settings
from ..utils.logging import get_logger
from typing import Optional

logger = get_logger(__name__)

class LLMClient:
    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.1-70b-versatile"):
        self.api_key = api_key or settings.groq_api_key
        if not self.api_key:
            logger.warning("GROQ_API_KEY is not set. LLM calls will fail without it.")
        self.model = model
        # Lazy import to avoid forcing dependency at import time
        try:
            from groq import Groq  # type: ignore
            self._client = Groq(api_key=self.api_key)
        except Exception as e:
            logger.error("Failed to initialize Groq client: %s", e)
            self._client = None

    async def chat(self, message: str, emotion: Optional[str] = None) -> str:
        if self._client is None:
            return "LLM unavailable (missing Groq client or API key)."
        prompt = build_prompt(message, emotion)
        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.6,
                max_tokens=512,
                stream=False,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            logger.error("Groq chat error: %s", e)
            return f"Error contacting LLM: {e}"
