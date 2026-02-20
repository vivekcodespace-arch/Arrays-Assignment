"""Question 2: Find the Maximum & Minimum Element

This file provides functions to find max and min elements.
"""

def find_max_min(arr):
    if not arr:
        return None, None
    return max(arr), min(arr)

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5]
    max_val, min_val = find_max_min(arr)
    print("Max:", max_val, "Min:", min_val)
