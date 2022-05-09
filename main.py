from argparse import ArgumentParser, Namespace
from libs.convert_video import ConvertVideo
from libs.convert_sequence import ConvertSequence
import os


def generate_gifsequence(convert: ConvertSequence, args: Namespace):

    convert.generate_palette(args.transparent)
    convert.to_gif()
    convert.clear_temp_files()

    if args.optimise:
        convert.optimize_gif(args.optimise)

    if args.lossy:
        convert.compress_gif(args.lossy)

    convert.print_output_info()


def generate_gifvideo(convert: ConvertVideo, args: Namespace):

    convert.generate_palette(args.transparent)
    convert.to_gif()
    convert.clear_temp_files()

    if args.optimise:
        convert.optimize_gif(args.optimise)

    if args.lossy:
        convert.compress_gif(args.lossy)


directory = os.getcwd() + "/InputImages/"


def main():

    args, _ = parse_args()

    sortDict = {"": []}

    for filename in os.listdir(directory):
        if ("_FRAME" not in filename):
            continue
        fileheader = filename.split("_FRAME")[0]

        if fileheader in sortDict:
            sortDict[fileheader].append(filename)
        else:
            sortDict[fileheader] = [filename]
            f_in = fileheader + "*.png"
            convert_sequence = ConvertSequence(
                directory+f_in, args.fps, fileheader)
            generate_gifsequence(convert_sequence, args)


def parse_args() -> tuple[Namespace, list]:

    parser = ArgumentParser(description='Converts video/sequence to GIF')
    parser.add_argument('-i', '--input', type=str, metavar='',
                        help='Input file path', required=False)

    parser.add_argument('-w', '--transparent', action='store_true',
                        help='Enable transparency', required=False)
    parser.add_argument('-l', '--lossy', type=str, default=None,
                        metavar='', help='No. of artefacts allowed', required=False)
    parser.add_argument('-z', '--optimise', type=int, default=None,
                        metavar='', help='Optimise GIF file size (1 - 3)', required=False)

    parser.add_argument('-a', '--assemble', action='store_true',
                        help='Assemble image sequence', required=False)
    parser.add_argument('-r', '--fps', type=int, default=50,
                        metavar='', help='Sequence FPS', required=False)

    return parser.parse_known_args()


if __name__ == '__main__':
    main()
