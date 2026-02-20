def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4]
    print(find_duplicates(arr))