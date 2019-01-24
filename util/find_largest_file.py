import os, glob, sys

fmt = '{0:<{ljust}}: {1}'

def get_file_sizes(directory=None, verbose=True, sort_by_size=True):
    '''
    Print python files and their sizes.
    You can choose to display the absolute filepaths or just the filenames using the verbose keyword.
    You can also choose to sort the output by file size using the sort_by_size keyword.
    '''
    global fmt

    # If theres no directory given, search python's source library
    dirname = directory if directory else os.path.dirname(sys.executable)+os.sep+'Lib'

    all_py_files = glob.glob(dirname + os.sep + '*.py')
    all_sizes = [os.path.getsize(filename) for filename in all_py_files]

    if verbose:
        filenames = all_py_files
    else:
        # get just the name of the file
        filenames = [filepath.split(os.sep)[-1] for filepath in all_py_files]

    # for nice formatting purposes
    longest_name = len(max(filenames, key=len))

    sorting_key = lambda t: t[1] if sort_by_size else None

    output = sorted(((filename, size) for filename, size in
                     zip(filenames, all_sizes)), key=sorting_key)


    for filename, size in output:
        print(fmt.format(filename, size, ljust=longest_name))

if __name__ == '__main__':
    directory = None if len(sys.argv) == 1 else sys.argv[1]
    get_file_sizes(directory)
