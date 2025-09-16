
def grouping_consecutive(val, arr):
    count = 0
    group = 0
    
    for i in arr:
        if i == val:
            count += 1
        else:
            group += count*(count+1)//2
            count = 0
    #last element
    group += count*(count+1)//2
    
    return group
    
# function to calculate the subarrays with sum = x 
# MOST OPTIMAL APPROACH - usiing Prefix Sum with Hashmaps
def subarr_sum(x, arr):
    subarr_count = 0
    prefix_sum = 0
    hashmap = {0:1}
    
    for num in arr:
        prefix_sum += num
        subarr_count += hashmap.get(prefix_sum, 0) # zero is the default value
        
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1 
        
    return subarr_count
        

def subarr_sum_without(x, arr):
    subarr_count = 0
    prefix_sum = 0
    hashmap = {0:1}
    
    for num in arr:
        if num == x:
            prefix_sum = 0
            hashmap = {0:1}
        else:
            prefix_sum += num
            subarr_count += hashmap.get(prefix_sum, 0)
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1 
        
    return subarr_count
            
    
t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    
    # subarrs of 1 combinations
    ans += grouping_consecutive(1, arr)
    # subarrs of 3 combinations
    ans += grouping_consecutive(3, arr)

    #### NOW NORMAL SUBARRAYS WITH 1,2,3
    
    """
        1 --> -1
        2 --> 0
        3 --> 1
    """
    for i in range(n):
        arr[i] -= 2
        
    # now finding the subarrs whose sum = 0, i.e the number of 1s and 3s are equal 
    ans += subarr_sum(0, arr) 
    # now removing the count of those subarrs whose sum = 0 but don't contain any 0 (i.e occurence of 2)
    ans -= subarr_sum_without(0, arr)

    print(ans)
    
    t-=1
