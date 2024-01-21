from loguru import logger

def tts(input_text):
    logger.info("Testing tts module")
    try:
        from src.modules.tts.tts_init import text_to_speech
        text_to_speech(input_text)
        logger.success("TTS module test passed")
    except:
        logger.exception("TTS module test failed")