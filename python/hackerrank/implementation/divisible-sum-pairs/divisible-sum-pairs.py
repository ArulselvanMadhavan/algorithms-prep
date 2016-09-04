"""Pure Python."""


def build_matrix(arr, n, k):
    """Build Sum Matrix."""
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                result.append((i, j))
    print(len(result))

if __name__ == '__main__':
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    build_matrix(a, n, k)
