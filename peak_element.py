def find_peak(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[-1] > arr[-2]:
        return arr[-1]
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return None

if __name__ == "__main__":
    arr = [1, 3, 20, 4, 1, 0]
    print(find_peak(arr))