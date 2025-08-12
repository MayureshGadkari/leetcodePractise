'''Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''

nums = [1,2,2,3,3,3]
k =2
def highest_freq(nums,k):
    count = {}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    sorted_list = list(dict(sorted(count.items(), key=lambda x: x[1])))
    print(sorted_list)
    print(count)
    return sorted_list[-k::]
print(highest_freq(nums,k))