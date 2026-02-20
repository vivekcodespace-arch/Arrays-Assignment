//Leader element problem
def find_leaders(arr):
    if not arr:
        return []
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.append(max_right)
    return leaders[::-1]

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print(find_leaders(arr))
