'''An attempt to replicate unix piping functionality

                example:
                python pipe.py "ls | sed <opts> | cut <opts> | sort <opts> | uniq"
'''
import argparse
import subprocess
import sys
import os


TMP_HANDLE = 'pipe_tmp.txt'


def main(args):
    '''main'''
    command_stream = ' '.join(args['cmds']).split('|')
    cmd, *opts = command_stream.pop(0).split()
    full_cmd = ['python', cmd+'.py']
    if opts:
        full_cmd += opts
    txt = subprocess.run(full_cmd, stdout=subprocess.PIPE).stdout
    write_to_temp(txt)

    for command in command_stream:
        cmd, *opts = command.strip().split()
        full_cmd = build_cmd(cmd, opts)
        txt = subprocess.run(full_cmd, stdout=subprocess.PIPE).stdout
        write_to_temp(txt)

    sys.stdout.write(txt.decode('utf-8'))

    os.remove(TMP_HANDLE)


def parse_args():
    '''parse the pipe expression'''
    desc = 'a program that simulates unix command-line pipe feature'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('cmds', type=str, nargs='+', help='a command that resembles a pipe stream. \
                        Enclose your pipe command in double-quotes(") otherwise it will not work.')
    return parser.parse_args()


def build_cmd(cmd, opts):
    '''This is necessary to parse commands together with the aforementioned temp file'''
    # fullCmd = ['python'] += shlex.split(command)         should try this one out too
    build = ["python", cmd+".py", TMP_HANDLE]
    if opts:
        build += opts
    return build


def write_to_temp(txt):
    ''' Going to be writing results to a temp file
    It helps keep track across the different changes we make
    For every command in the stream we run on the file
    '''
    # Considered using the tempfile module but the code I used for it was very repetitious
    text = txt.decode('utf-8').split('\r')
    with open(TMP_HANDLE, 'w') as tmp:
        for line in text:
            tmp.write(line)


if __name__ == '__main__':
    main(vars(parse_args()))
