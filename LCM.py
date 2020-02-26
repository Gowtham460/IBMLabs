def compute_lcm(x, y):
    if x > y:
        l = x
    else:
        l = y
    while True:
        if (l % x == 0) and (l % y == 0):
            lcm = l
            break
        l += 1
    return lcm


n = int(input("Enter the number:"))
m = int(input("Enter the next number:"))
print(compute_lcm(n, m))
