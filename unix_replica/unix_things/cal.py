import argparse
import calendar
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true', help='first day is sunday')
    parser.add_argument('-m', action='store_true', help='first day is monday')
    parser.add_argument('-3', action='store_true', default=True, help='display three months')
    parser.add_argument('-y', action='store_true', help='display calendar for the whole year')
    parser.add_argument('-Y', action='store_true', help='display calendar for the next 12 months')

    return parser.parse_args()


# def iterate_months(year)


def main(args):
    year_month = "%Y %m"
    year, month = [int(t) for t in time.strftime(year_month).split()]

    calendar.setfirstweekday(0)
    if args['s']:
        calendar.setfirstweekday(6)

    if not args['y'] or args['Y']:
        sys.stdout.write(calendar.month(year, month))
    elif args['y']:
        sys.stdout.write(calendar.calendar(year))




if __name__ == '__main__':
    main(vars(parse_args()))
