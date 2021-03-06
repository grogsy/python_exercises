import os, glob, sys

fmt = '{0:<{ljust}}: {1}'

def get_file_sizes(directory, verbose=True, sort_by_size=True):
    '''
    Print python files and their sizes.
    You can choose to display the absolute filepaths or just the filenames using the verbose keyword.
    You can also choose to sort the output by file size using the sort_by_size keyword.
    '''
    global fmt

    # If theres no directory given, search python's source library
    dirname = directory

    all_py_files = glob.glob(dirname + os.sep + '*.py')
    all_sizes = [os.path.getsize(filename) for filename in all_py_files]

    if verbose:
        filenames = all_py_files
    else:
        # get just the name of the file
        filenames = [filepath.split(os.sep)[-1] for filepath in all_py_files]

    # for nice formatting purposes, get the longest name in the names list
    longest_name = len(max(filenames, key=len))

    # lambda function to use size in (file, size) tuple as key for sorted()
    sorting_key = lambda t: t[1] if sort_by_size else None

    output = sorted(((filename, size) for filename, size in
                     zip(filenames, all_sizes)), key=sorting_key)


    for filename, size in output:
        print(fmt.format(filename, size, ljust=longest_name))


def scan_standard_library(sort_by_size=True):
    global fmt
    directory = os.path.dirname(sys.executable)+os.sep+'Lib'

    all_sizes = []
    all_py_files = []

    for (current_directory, sub_directories, files_here) in os.walk(directory):
        for filename in files_here:
            if filename.endswith('.py'):
                fullname = os.path.join(current_directory, filename)
                all_py_files.append(fullname)
                all_sizes.append(os.path.getsize(fullname))

    longest_name = len(max(all_py_files, key=len))

    sorting_key = lambda t: t[1] if sort_by_size else None

    output = sorted(((filename, size) for filename, size in
                     zip(all_py_files, all_sizes)), key=sorting_key)

    for filename, size in output:
        print(fmt.format(filename, size, ljust=longest_name))



if __name__ == '__main__':
    directory = os.path.dirname(sys.executable)+os.sep+'Lib' if len(sys.argv) == 1 else sys.argv[1]
    #get_file_sizes(directory)
    scan_standard_library()
