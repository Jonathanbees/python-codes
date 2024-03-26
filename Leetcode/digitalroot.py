def digital_root(n):
    nums = []
    n = int(n)
    while n > 0:
        nums.append(n % 10)
        n = n // 10
    suma = sum(nums)
    print(suma)
    if suma > 9:
        return digital_root(suma)
    else:
        return suma

digital_root("16")

print(1%10)
print(1//10)