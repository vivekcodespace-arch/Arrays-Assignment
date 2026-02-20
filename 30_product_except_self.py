# Question 30: Product of Array Except Self
def product_except_self(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * arr[i+1]
    return [left[i] * right[i] for i in range(n)]

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(product_except_self(arr))