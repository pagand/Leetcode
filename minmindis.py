# Problem:
# Given locations of stores as a list of integers, find two apartment locations such that the distance between stores to the nearest apartment is minimized.


# break down the problem:
# Case 1: we are looking for the integer positions for the two apartments
# Case 2: Location of the apartments can be any flout value.

# Approach for Case 1:
# 1. Brute force approach:
# 1.1. two nested loops, each looping over the stores, compute two distance, find the min, add to the distance_sum, and track min so far.
# 1.2. Time complexity: O(n^2), Space complexity: O(1)
# 2. Optimal approach: 
# The solution to each subproblem is its median, so the question is to find the split point. We can start by assigning it to median, then
#  move it to the left or right based on the distance between the median and the stores. 
# 2.1. Sort the stores
# 2.2. Find the median of the stores
# 2.3. Assign the median to the split point, find the median for left and right split
# 2.4. Compute the distance for each split, if left/right split is larger, move the split point to the left/right to include one more store.

def median(array):
    if len(array)%2 == 1:
        ind = int((len(array)-1)/2)
        median =  array[ind]
    else:
        ind = int(len(array)/2)
        median = (array[ind] + array[ind-1] )/2
    sum = 0
    for x in array:
        sum += abs(median - x)
    return ind, sum


def minmindis(stores):
    # sort the stores
    stores_sorted = sorted(stores)
    # find the median and assign to split
    split, _ = median(stores_sorted)
    # left and right
    _, leftd = median(stores_sorted[:split])
    _, rightd = median(stores_sorted[split:])
    minumum = 1000
    minsofar = leftd + rightd
    while minumum>minsofar:
        minumum = minsofar
        if rightd>leftd and split<len(stores_sorted):
            split +=1
        elif leftd>rightd and split>0:
            split -=1    
        _, leftd = median(stores_sorted[:split])
        _, rightd = median(stores_sorted[split:])  
        minsofar =  leftd + rightd
    return minumum



if __name__ == "__main__":
    stores = [4,8,0,6]
    apartments = []
    apartments = minmindis(stores)
    print(apartments)