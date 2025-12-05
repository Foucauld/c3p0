#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import time

import sounddevice as sd

from vosk import Model, KaldiRecognizer
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

q = queue.Queue()


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def substring_after(s, delim):
    return s.split(delim)


def run(args):
    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info["default_samplerate"])

        if args.model is None:
            model = Model(lang="en-us")
        else:
            model = Model(lang=args.model)

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        recognized_text = ""
        with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                               dtype="int16", channels=1, callback=callback), open('assets/bell.wav', 'rb') \
                as audio_file:
            audio_segment = AudioSegment.from_file(audio_file, format="wav")
            play(audio_segment)
            rec = KaldiRecognizer(model, args.samplerate)
            rec.SetWords(False)
            keepGoing = True
            while keepGoing:
                data = q.get()
                if rec.AcceptWaveform(data):
                    recognized_text += substring_after(rec.Result(), '"')[3]
                    # here the result is printed
                    keepGoing = False
                if dump_fn is not None:
                    dump_fn.write(data)
            print(recognized_text)
            play(audio_segment)
            return recognized_text
    except KeyboardInterrupt:
        print("\nDone")
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))


