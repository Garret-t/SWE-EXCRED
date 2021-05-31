#This was the very first leetcode problem I tried a year ago
#I still remember my first solution and the optimal!

#Brute-force
def two_sum(array, target_sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]

#Optimal - Hash maps
def two_sum_optimal(array, target_sum):
    hash_map = {}
    for i in range(len(array)):
        comp = target_sum - array[i]
        if comp in hash_map:
            return [array[i], comp]
        hash_map[array[i]] = 1
        
print(two_sum([2, 7, 11, 15], 17))
print(two_sum_optimal([2, 7, 11, 15], 17))