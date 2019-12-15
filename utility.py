import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser(
        prog='utility',
        description='''This is test program''',
        epilog='''(c) CoolCoderCarl'''
    )
    parser.add_argument('-n','--name', default='world')
    parser.add_argument('-c','--count', type=int, default=1)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])


    for _ in range(namespace.count):
        print("Hello, {}!".format(namespace.name))

