"""Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first."""


#This approach failed as there can me duplicate index with same number and it will always provide the first index

nums = [3,4,5,6]
target = 7
def two_sum(nums,target):
    for i in range(len(nums)):
        to_find = target - nums[i]
        if to_find in nums:
            return [i,nums.index(to_find)]
print(two_sum(nums,target))

def two_sum_factored(nums,target):
    hashmap = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return[hashmap[diff],i]
        hashmap[num]=i

print(two_sum_factored(nums,target))
