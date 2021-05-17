#!/usr/bin/env python3
# Font to HTML 1.0
# @author Metrobyte, https://metrobyte.ru, https://github.com/MetroByte/GetFontChars

"""Create text file with all font supported characters."""
import argparse
from fontTools import ttLib


def get_chr_list(font, print_chars=False):
    """Return UTF-8 list of characters and char count"""
    chars = ''
    cmap = font['cmap'].getBestCmap()
    for key in cmap:
        chars += chr(key)
    if print_chars:
        print(chars)
    return chars, len(chars)


def main():
    # commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--page', help='Font page if multipage font', default=0)
    parser.add_argument('-t', '--print', help='Print list of character to console', default=False, nargs='?')
    parser.add_argument(
        '-o', '--output', help='Output UTF-8 txt file', default='')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument(
        '-i', '--input', help='Input font file', required=True)    

    args = parser.parse_args()

    # 'False' when -t is not used at all
    if args.print != False:
        args.print = True

    if not args.print and (args.output == ''):
        raise ValueError("Specify output file or use -t to print character list in console output")

    if args.page == '' or args.page is None:
        font = ttLib.TTFont(args.input)
    else:
        font = ttLib.TTFont(args.input, fontNumber=int(args.page))

    chr_str, chr_len = get_chr_list(font, args.print)

    print(f'Font file {args.input} contains {chr_len} characters.')

    if args.output != '':
        with open(args.output, mode='wt', encoding='utf-8') as f:
            f.write(chr_str)
    elif (args.output == '') and not args.print:
        raise IOError("Output file must be specified with -o")


if __name__ == '__main__':
    main()
