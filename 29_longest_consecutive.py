# Question 29: Find the Longest Consecutive Sequence
def longest_consecutive(arr):
    if not arr:
        return 0
    arr = set(arr)
    max_length = 0
    for num in arr:
        if num - 1 not in arr:
            current = num
            length = 1
            while current + 1 in arr:
                current += 1
                length += 1
            max_length = max(max_length, length)
    return max_length

if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(arr))