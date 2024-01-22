from dotenv import load_dotenv
from TTS.api import TTS


def text_to_speech(input_text):
    import os
    load_dotenv()
    use_gpu = os.environ["use_gpu"]
    if use_gpu == "False":
        use_gpu = False
    else:
        use_gpu = True

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
    import soundfile as sf
    import sounddevice as sd
    audio_file_dir = "audio_dirs/output.wav"
    data, fs = sf.read(audio_file_dir, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()

    os.remove(audio_file_dir)