
from ..config import settings
from ..utils.logging import get_logger

logger = get_logger(__name__)

class EmotionService:
    def __init__(self):
        # Lazy import DeepFace to avoid heavy import when unused
        try:
            from deepface import DeepFace  # type: ignore
            self.DeepFace = DeepFace
        except Exception as e:
            logger.error("Failed to import DeepFace: %s", e)
            self.DeepFace = None

    async def analyze(self, image_array):
        if self.DeepFace is None:
            raise RuntimeError("DeepFace not available")
        try:
            result = self.DeepFace.analyze(
                img_path = image_array,  # ndarray is accepted
                actions = ['emotion'],
                detector_backend = settings.deepface_detector or 'opencv',
                enforce_detection=False
            )
            # DeepFace returns list or dict depending on version
            data = result[0] if isinstance(result, list) else result
            emo_prob = data.get('emotion', {}) or data.get('emotions', {})
            if not emo_prob:
                return {"dominant_emotion":"neutral", "confidence":0.0, "raw": data}
            dominant = max(emo_prob, key=emo_prob.get)
            confidence = float(emo_prob.get(dominant, 0.0))
            return {
                "dominant_emotion": dominant,
                "confidence": confidence,
                "raw": data
            }
        except Exception as e:
            logger.error("DeepFace analyze error: %s", e)
            return {"dominant_emotion":"neutral", "confidence":0.0, "raw":{"error": str(e)}}
