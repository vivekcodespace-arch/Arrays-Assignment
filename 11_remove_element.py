# Question 11: Remove given Element from Array
def remove_element(arr, val):
    return [x for x in arr if x != val]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2]
    val = 2
    print(remove_element(arr, val))