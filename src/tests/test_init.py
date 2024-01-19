from loguru import logger

def tts():
    logger.info("Testing tts module")
    try:
        from src.modules.tts.tts_init import text_to_speech
        text_to_speech("This is an amazing test message")
        logger.success("TTS module test passed")
    except:
        logger.exception("TTS module test failed")