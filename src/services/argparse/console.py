import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--j", type=int, help="the code", required=True)

args = vars(parser.parse_args())

print("####################\n")
code = args["j"]

if code == 18:
    print("here it goes our json")
else:
    print("error")
