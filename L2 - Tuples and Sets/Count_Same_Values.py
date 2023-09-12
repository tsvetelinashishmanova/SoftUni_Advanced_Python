numbers = tuple([float(x) for x in input().split()])
nums = {}

for num in numbers:
    if num not in nums:
        nums[num] = 0
    nums[num] += 1

for key, value in nums.items():
    print(f"{key:.1f} - {value} times")
