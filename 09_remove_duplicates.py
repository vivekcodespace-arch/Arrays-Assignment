# Question 09: Remove Duplicates from Array
def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 5]
    print(remove_duplicates(arr))