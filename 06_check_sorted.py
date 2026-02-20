# Question 06: Check if Array is Sorted
def is_sorted(arr):
    return arr == sorted(arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Is sorted:", is_sorted(arr))