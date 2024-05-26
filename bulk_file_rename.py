import argparse
import glob
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='Directory to rename files in, e.g. D:/Work/', required=True)
    parser.add_argument('-p', '--pattern', help='Pattern to search files in directory, e.g. `*.out`', required=True)
    parser.add_argument('-e', '--extension', help='File extension to rename files to, e.g. `log`', required=True)
    args = parser.parse_args()

    directory = args.dir if args.dir.endswith('/') or args.dir.endswith('\\') else f'{args.dir}/'
    pattern = args.pattern
    new_extension = args.extension if args.extension.find('.') > 0 else f'.{args.extension}'

    print(f'Working directory: {directory}')
    matched = glob.glob(directory + pattern)
    for filepath in matched:
        full_filename = filepath[filepath.rfind('\\') + 1:]
        filename = full_filename[:full_filename.find('.')]
        print(f'Renaming {full_filename} to {filename}{new_extension}')

        os.rename(directory + full_filename, directory + filename + new_extension)
