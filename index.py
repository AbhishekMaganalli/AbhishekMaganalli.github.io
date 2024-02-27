
def topKFrequent( nums,k) :
    map = dict()
    unique_set = list(set(nums))
    for i in range(len(unique_set)):
        map[unique_set[i]]=0
    for i in range(len(nums)):
        map[nums[i]]+=1
    return map

print(topKFrequent([4,4,4,4,4,4,77,7,7,7,7,1,2,3,4], 2))

