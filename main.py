import os
from gtts import gTTS
from playsound import playsound

if __name__ == '__main__':
    answer = "test"

    """ 
    Start voice pipeline
    """
    from src.client_pipeline import tts_pipeline
    vocal_pipeline = tts_pipeline()
    vocal_pipeline.tts(answer, save_path=f'./audio_cache/dialog_cache.wav', voice_conversion=True)
    print("test")