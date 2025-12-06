import pyttsx3
import simpleaudio as sa
import os

RESPONSES_DIR = "assets/responses"


def play_response(filename):
    """
    Joue un fichier WAV depuis le dossier RESPONSES_DIR.
    """
    filepath = os.path.join(RESPONSES_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Fichier {filepath} introuvable, fallback TTS.")
        return False

    wave_obj = sa.WaveObject.from_wave_file(filepath)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # attendre la fin de la lecture
    return True


def respond_tts(text):
    """
    Fallback synthèse vocale via pyttsx3 si WAV manquant.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "fr")  # ajuster selon votre système
    engine.say(text)
    engine.runAndWait()


def pick_response(command, location: str = None):
    """
    Retourne le nom du fichier WAV correspondant à la commande.
    Si location est fourni, il est utilisé pour générer le nom du fichier.
    """
    if not command:
        return "UNKNOWN.wav"
    return f"{command}.wav"


def execute_response(command, fallback_text: str = None):
    """
    Joue la réponse audio correspondante à la commande.
    """
    filename = pick_response(command)
    if not play_response(filename):
        if fallback_text is None:
            fallback_text = command.replace("_", " ").capitalize()
        respond_tts(fallback_text)


def list_available_voices():
    """
    Affiche les voix disponibles pour pyttsx3.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for i, voice in enumerate(voices):
        print(f"Voice {i + 1}:")
        print(f" - ID: {voice.id}")
        print(f" - Name: {voice.name}")
        print(f" - Languages: {voice.languages}")
        print(f" - Gender: {voice.gender}")
        print(f" - Age: {voice.age}")
        print("\n")
