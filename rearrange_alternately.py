//Rearranging with better time complexity
def rearrange_alternately(arr):
    arr.sort()
    result = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if left <= right:
            result.append(arr[right])
            right -= 1
        if left <= right:
            result.append(arr[left])
            left += 1
    return result

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(rearrange_alternately(arr))
