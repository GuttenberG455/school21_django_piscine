from antigravity import geohash
import sys


def show_geohash(args):

    try:
        latitude = float(args[1])
        longitude = float(args[2])
    except ValueError:
        return print("First and second arguments (latitude, longitude) should be float!")
    try:
        date = args[3].encode("UTF-8")
    except:
        return print("Third argument should be string (yyyy-mm-dd)")
    geohash(latitude, longitude, date)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        show_geohash(sys.argv)
    else:
        print("Wrong Input! Three arguments required: latitude, longitude, date (yyyy-mm-dd)")

# python3 geohashing.py 51.389079 30.1007360 1986-04-26-322.16
