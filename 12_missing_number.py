# Question 12: Find the Missing Number
def find_missing(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

if __name__ == "__main__":
    arr = [1, 2, 4, 5]
    n = 5
    print("Missing:", find_missing(arr, n))