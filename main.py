if __name__ == '__main__':
    print("Would you like to test all modules? (y/n)")

    if input().lower() == "y":
        try:
            import time
            from loguru import logger
            import src.tests.test_init as test_init
            import src.tests.ai_chat as ai_chat

            test_init.tts("This is an amazing test message")

            logger.info("Testing AI chat...")
            ai_output = ai_chat.test_ai_chat()

            logger.info("Testing TTS with AI output...")
            if ai_output:
                test_init.tts(ai_output)
            else:
                logger.warning("AI output is empty. Unable to perform TTS.")

            logger.success("All tests passed 👍")
            exit()
        except Exception as e:
            logger.error(f"An error occurred during tests 😢.\n\n{e}")
            exit()

    answer = "This is an amazing test message"

    """ 
    Generate TTS
    """
    from src.modules.tts.tts_init import text_to_speech
    text_to_speech(answer)