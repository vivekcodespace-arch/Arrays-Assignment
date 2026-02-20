from collections import Counter

def count_frequency(arr):
    return dict(Counter(arr))

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3]
    print(count_frequency(arr))