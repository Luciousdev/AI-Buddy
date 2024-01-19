from dotenv import load_dotenv
from TTS.api import TTS



def text_to_speech(input_text):
    import os
    load_dotenv()
    use_gpu = os.environ["use_gpu"]
    print(use_gpu)
    """
        Generate TTS
    """
    # Load model
    tts = TTS(model_name="tts_models/en/jenny/jenny", gpu=use_gpu)
    tts.to()
    # Synthesize text
    tts.tts_to_file(text=input_text, file_path="audio_dirs/output.wav")

    """
        Process the audio file
    """
    # Play the audio file
    from playsound import playsound
    playsound("audio_dirs/output.wav")
    # Remove the audio file
    import os
    os.remove("audio_dirs/output.wav")