from argparse import ArgumentParser
from collections import Counter

def parse_line(line):
    return line.split()[0]

def check_labels(labels):
    assert labels[0] == 1
    idx = 1
    while labels[idx] == 1:
        idx += 1
    count = idx
    while idx < len(labels):
        assert labels[idx] == 0
        idx += 1
    return count

def parse_file(file_name):
    labels = [parse_line(line) for line in open(file_name)]
    labels = map(int, labels)
    counts = []
    assert len(labels) % 500 == 0
    for i in range(len(labels) // 500):
        count = check_labels(labels[i * 500: (i + 1) * 500])
        counts.append(count)
    print('\n'.join(map(str, sorted(counts, reverse=True))))

def main():
    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    parse_file(args.input)

if __name__ == '__main__':
    main() 
    
