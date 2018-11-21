prefixes = {
    1024   : 'kB',
    1024**2: 'MB',
    1024**3: 'GB'
}


def str_fmt_filesize(size, trunc=False):
    '''Translate file size number to english'''
    key = None
    for size_number in sorted(prefixes.keys()):
        if size >= size_number:
            key = size_number
        else:
            break

    if not key:
        prefix = 'bytes'
    else:
        prefix = prefixes[key]
        if trunc:
            size = size//key
        else:
            size = size/key

    fmt = '{:.1f} {}'

    return fmt.format(size, prefix)
