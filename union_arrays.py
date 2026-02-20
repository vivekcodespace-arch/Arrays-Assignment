def union(a, b):
    return list(set(a) | set(b))

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [3, 4, 5]
    print(union(a, b))