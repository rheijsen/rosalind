def motif_finder(s, t):
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            print(i+1, end=' ')

if __name__ == '__main__':
    s = "GATATATGCATATACTT"
    t = "ATAT"
    motif_finder(s, t)

