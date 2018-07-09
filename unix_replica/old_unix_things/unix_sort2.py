import argparse
from operator import itemgetter

# note: nargs ---> number of arguments 

def parse_args():
    parser = argparse.ArgumentParser(description='Sort file text')

    parser.add_argument('files', type=str, nargs='+')

    parser.add_argument('-n', action='store_true', help='Sort by numerical value')

    parser.add_argument('-k', type=int, nargs='+', help='Sort by a specified key(s). Numbers will sort by column(start indices by 0)')

    parser.add_argument('-r', action='store_true', help='Sort in reverse')

    parser.add_argument('-f', action='store_true', help='Ignore case')

    return parser.parse_args()


def sort_by_key(txt, args):
    if args['n']:
        txt = sort_by_num(txt)
    if args['k']:
        column = args['k']
        txt = sort_by_column(txt, column)
    return txt


def sort_by_column(txt, column):
    column_key = itemgetter(*column)
    try:
        # Sometimes we don't know if the column is all integers, characters, or a mix
        # Defaulting to sorting by string representation seems safer(so far)
        try:
            return sorted(txt, key=lambda s: int(column_key(s.split())))
        except (ValueError, TypeError):
            input("Attempt to sort numerically failed, sorting done as if string")
            return sorted(txt, key=lambda s: column_key(s.split()))
    except:
        input("Unable to sort by column.")


def sort_by_num(txt):
    try:
        # sorted implicitly sorts numerics before other characters besides whitespace
        return sorted(txt, key=lambda s: sorted(s.strip().split()))
    except:
        input("Unable to sort numerically.")


if __name__ == '__main__':
    args = vars(parse_args())
    files = args.pop('files')
    for file in files:
        with open(file, 'r') as cur:
            txt = sorted(cur.readlines())
            if args['k'] or args['n']:
                txt = sort_by_key(txt, args)
            if args['f']:
                txt = sorted(txt, key=lambda s: s.casefold())
            if args['r']:
                txt = reversed(txt)
            print('\n'.join(txt))
