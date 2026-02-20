//1st code
def all_subarrays(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subarrays.append(arr[i:j])
    return subarrays

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(all_subarrays(arr))
