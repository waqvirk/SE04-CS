### Two Sum ###

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_opt(nums, target):
    seen = {}
    for i, num in enumerate(nums):  # keep track of index and value
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # return indices
        seen[num] = i  # store index, not the number itself

# Example 1
nums = [2,7,11,15]
target = 9

print("Brute Force Approach O(n²):", two_sum(nums, target))
print("Optimized Hash Map O(n):", two_sum_opt(nums, target))

# Example 2
nums = [3,2,4]
target = 6

print("Brute Force Approach O(n²):", two_sum(nums, target))
print("Optimized Hash Map O(n):", two_sum_opt(nums, target))

# Example 3
nums = [3,3]
target = 6

print("Brute Force Approach O(n²):", two_sum(nums, target))
print("Optimized Hash Map O(n):", two_sum_opt(nums, target))