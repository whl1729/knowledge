import argparse
parser = argparse.ArgumentParser(description="what the program does")
# add a positional integer argument
parser.add_argument("square", type=int,
                    help="display a square of a given number")
# add a optional boolean argument
parser.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="increase output verbosity")
# add a optional integer argument (The default type is "str")
parser.add_argument("-p", "--port", type=int, default=8080,
                    help="port number of the server")
# add a optional string argument
parser.add_argument("-n", "--name",
                    help="host name of the server")
args = parser.parse_args()


# Reference: https://docs.python.org/3/library/argparse.html
