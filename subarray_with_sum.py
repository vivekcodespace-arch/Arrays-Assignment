def subarray_sum(arr, target):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return arr[start:end+1]
    return None

if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    target = 33
    print(subarray_sum(arr, target))