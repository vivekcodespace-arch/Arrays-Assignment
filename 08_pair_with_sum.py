# Question 08: Find Pair with Given Sum
def find_pair(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return [target - num, num]
        seen.add(num)
    return None

if __name__ == "__main__":
    arr = [1, 4, 5, 11, 12]
    target = 9
    print(find_pair(arr, target))