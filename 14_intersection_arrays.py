# Question 14: Find the Intersection of Two Arrays
def intersection(a, b):
    return list(set(a) & set(b))

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print(intersection(a, b))