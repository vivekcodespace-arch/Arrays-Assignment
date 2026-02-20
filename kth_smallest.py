//Optimized solution 
def kth_smallest(arr, k):
    return sorted(arr)[k-1]

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(kth_smallest(arr, k))
