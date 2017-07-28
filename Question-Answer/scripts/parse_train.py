from argparse import ArgumentParser
from collections import Counter

def parse_line(line):
    return line.split()[2]

def parse_file(file_name):
    q_count = Counter()
    with open(file_name) as fn:
        for line in fn:
            q_count[parse_line(line)] += 1
    q_count = sorted(q_count.items(), key=lambda x:x[1], reverse=True)
    print('\n'.join('\t'.join(map(str, item)) for item in q_count))

def main():
    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    parse_file(args.input)

if __name__ == '__main__':
    main()
