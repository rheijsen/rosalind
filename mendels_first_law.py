def mendels(k, m, n):
    total = k + m + n
    print(1 - (m * n + 0.25 * m * (m - 1) + n * (n - 1)) / (total * (total - 1)))


if __name__ == '__main__':
    k = 17
    m = 28
    n = 15
    mendels(k, m, n)
