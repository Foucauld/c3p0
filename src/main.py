import pvporcupine
import pyttsx3

import arguments as arg

from wake_word import WakeWord


def main():
    args = arg.init_args()

    if args.show_audio_devices:
        WakeWord.show_audio_devices()
    else:
        if args.access_key is None:
            raise ValueError("AccessKey (--access_key) is required")
        if args.keyword_paths is None:
            if args.keywords is None:
                raise ValueError(
                    "Either `--keywords` or `--keyword_paths` must be set."
                )

            keyword_paths = [pvporcupine.KEYWORD_PATHS[x] for x in args.keywords]
        else:
            keyword_paths = args.keyword_paths

        if args.sensitivities is None:
            args.sensitivities = [0.5] * len(keyword_paths)

        if len(keyword_paths) != len(args.sensitivities):
            raise ValueError(
                "Number of keywords does not match the number of sensitivities."
            )

        WakeWord(
            access_key=args.access_key,
            library_path=args.library_path,
            model_path=args.model_path,
            keyword_paths=keyword_paths,
            sensitivities=args.sensitivities,
            args=args,
            output_path=args.output_path,
            input_device_index=args.audio_device_index,
        ).run()


if __name__ == "__main__":
    main()
