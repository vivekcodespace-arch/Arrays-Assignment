# Question 10: Merge Two Sorted Arrays
def merge_sorted(a, b):
    return sorted(a + b)

if __name__ == "__main__":
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(merge_sorted(a, b))