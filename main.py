import sys
import PyPunch

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])
    while len(args):
        PyPunch.build_card(sys.argv.pop())
