import src.modules.aichat.init as aichat_init
from loguru import logger


def test_ai_chat():
    logger.info("Starting AI Chat Tests")
    try:
        aichat = aichat_init.generate_chat("Hello how are you doing?")
        logger.success("AI Chat test was successful")
        return aichat
    except:
        logger.exception("Something went wrong while generating the AI chat.")