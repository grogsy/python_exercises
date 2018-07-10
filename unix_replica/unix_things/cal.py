import argparse
import calendar
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('day', nargs='?', type=int)
    parser.add_argument('month', nargs='?', type=int)
    parser.add_argument('year', nargs='?', type=int)
    parser.add_argument('-s', action='store_true', help='first day is sunday')
    parser.add_argument('-m', action='store_true', default=True, help='first day is monday')
    parser.add_argument('-3', action='store_true', help='display three months')
    parser.add_argument('-y', action='store_true', help='display calendar for the whole year')
    parser.add_argument('-Y', action='store_true', help='display calendar for the next 12 months')
    parser.add_argument('-n', type=int, help='display next n months')

    return parser.parse_args()


def iterate_months(year, month, amt):
    for _ in range(amt):
        sys.stdout.write(calendar.month(year, month))
        month += 1
        if month >= 13:
            month = 1
            year += 1


def main(args):
    if not (args['year'] and args['month']):
        # Get the current date
        year, month = [int(t) for t in time.strftime("%Y %m").split()]
    else:
        year, month = args['year'], args['month']

    calendar.setfirstweekday(0)
    if args['s']:
        calendar.setfirstweekday(6)

    if args['y']:
        sys.stdout.write(calendar.calendar(year))
    elif args['Y']:
        iterate_months(year, month, 12)
    elif args['3']:
        iterate_months(year, month, 3)
    elif args['n']:
        iterate_months(year, month, args['n'])
    else:
        sys.stdout.write(calendar.month(year, month))


if __name__ == '__main__':
    main(vars(parse_args()))
