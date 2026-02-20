# Question 25: Find Majority Element
def majority_element(arr):
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    # Verify
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

if __name__ == "__main__":
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(majority_element(arr))