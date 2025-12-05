import argparse
import sounddevice as sd


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def init_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l",
        "--list-devices",
        action="store_true",
        help="show list of audio devices and exit",
    )
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser],
    )

    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        metavar="FILENAME",
        help="audio file to store recording to",
    )
    parser.add_argument(
        "-d", "--device", type=int_or_str, help="input device (numeric ID or substring)"
    )
    parser.add_argument("-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        help="language model; e.g. en-us, fr, nl; default is en-us",
    )

    parser.add_argument(
        "--access_key",
        required=True,
        help="AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)",
    )

    parser.add_argument(
        "--keyword_paths",
        nargs="+",
        required=True,
        help="Absolute or relative paths to keyword model files (.ppn)",
    )

    parser.add_argument(
        "--library_path",
        type=str,
        default=None,
        help=(
            "Absolute path to the Porcupine dynamic library (.so/.dll/.dylib). "
            "If None, pvporcupine will use the default for your platform."
        ),
    )

    parser.add_argument(
        "--model_path",
        type=str,
        default=None,
        help=(
            "Absolute path to the Porcupine parameters file (.pv). "
            "If None, pvporcupine will use the default for your platform."
        ),
    )

    parser.add_argument(
        "--sensitivities",
        nargs="+",
        type=float,
        default=None,
        help=(
            "Sensitivities for detecting keywords. Each value should be in [0,1]. "
            "If not set, defaults to 0.5 for all keywords."
        ),
    )

    parser.add_argument(
        "--audio_device_index",
        type=int,
        default=-1,
        help="Index of input audio device.",
    )

    parser.add_argument(
        "--output_path",
        type=str,
        default=None,
        help="Absolute path to recorded audio file (for debugging).",
    )

    parser.add_argument(
        "--show_audio_devices",
        action="store_true",
        help="Show available audio devices and exit.",
    )

    return parser.parse_args(remaining)
