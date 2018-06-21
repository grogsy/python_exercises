'''An attempt to replicate unix piping functionality
requirements:

            command piping should be read from left to right
            an example would be something like:
                -history | sed <file_arg> <opts> | cut <opts> | sort <opts> | uniq

            -keeping this in mind, we start by implementing functionality for one type of arg
            and this will be a single text file to process across the pipe
'''
import argparse
import subprocess
import sys


# Going to be writing results to a temp file
# It helps keep track across the different changes we make
# For every command in the stream we run on the file
TMP_HANDLE = 'pipe_tmp.txt'

def main(args):
    command_stream = ' '.join(args['c']).split('|')

    initCmd, *initOpts = command_stream.pop(0).split()
    txt = subprocess.run(build_cmd(initCmd, initOpts, args['file']), stdout=subprocess.PIPE).stdout
    write_to_temp(txt)

    for command in command_stream:
        cmd, *opts = command.strip().split()
        fullCmd = build_cmd(cmd, opts)
        txt = subprocess.run(fullCmd, stdout=subprocess.PIPE).stdout
        write_to_temp(txt)

    sys.stdout.write(txt.decode('utf-8'))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='the file to process')
    parser.add_argument('-c', type=str, nargs='+', help='a command that parses a pipe stream. \
                        Enclose your pipe command in double-quotes(") otherwise it will not work.')
    return parser.parse_args()


def build_cmd(cmd, opts, f=None):
    '''expected output: python cmd.py file.txt -o opt -foo bar.split()'''
    # fullCmd = ['python'] += shlex.split(command)         should try this one out too
    if not f:
        f = TMP_HANDLE
    build = ["python", cmd+".py", f]
    if opts:
        build += [opt for opt in opts.split()]
    return build


def write_to_temp(txt):
    with open(TMP_HANDLE, 'r+') as tmp:
        tmp.seek(0)
        tmp.write(txt.decode('utf-8'))


if __name__ == '__main__':
    main(vars(parse_args()))
