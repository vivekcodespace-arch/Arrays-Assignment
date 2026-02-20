def arrays_equal(a, b):
    return sorted(a) == sorted(b)

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [3, 2, 1]
    print("Equal:", arrays_equal(a, b))