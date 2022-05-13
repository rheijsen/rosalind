def compute_gc_content(file):
    max_gc = 0.0

    with open(file) as f:
        content = f.readlines()
        for i, line in enumerate(content):
            if line.startswith('>'):
                id = line[1:]
                seq = ''
            else:
                newseq = line.strip()
                seq = seq + newseq
                if i == len(content) - 1 or content[i + 1].startswith('>'):
                    gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                    if gc > max_gc:
                        max_gc = gc
                        max_id = id

    print(max_id.strip())
    print(max_gc)


if __name__ == '__main__':
    file = "datasets/rosalind_gc.txt"
    compute_gc_content(file)