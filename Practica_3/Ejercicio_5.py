nums = []
for i in range(11):
    nums.append(i)
nums.sort(reverse=True)
for x in nums:
    if x > 0:
        print(x, end=", ")
    else:
        print(x)