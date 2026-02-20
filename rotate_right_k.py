def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    print(rotate_right(arr, k))