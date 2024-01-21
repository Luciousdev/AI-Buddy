if __name__ == '__main__':
    print("Would you like to test all modules? (y/n)")

    if input().lower() == "y":
        import src.tests.test_init as test_init
        test_init.tts()

        exit()


    answer = "This is an amazing test message"

    """ 
    Generate TTS
    """
    from src.modules.tts.tts_init import text_to_speech
    text_to_speech(answer)