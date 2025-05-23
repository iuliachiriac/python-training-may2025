import argparse


parser = argparse.ArgumentParser(description='Argparse example')
parser.add_argument('number', type=int, help='do something with number')
parser.add_argument('--flag', help='flag stored true if present',
                    action='store_true')

args = parser.parse_args()
print(args.number, args.flag)
