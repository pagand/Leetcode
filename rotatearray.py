class Solution(object):
    def _rotate(self,nums,k, s):
        min_visited = len(nums)
        pos = s
        cur = nums[pos]
        pos = (pos + k) % len(nums) 
        while pos != s:
            if pos<min_visited:
                min_visited = pos
            cur2 = nums[pos]
            nums[pos] = cur
            cur = cur2
            pos = (pos + k) % len(nums)
        nums[s] = cur
        return min_visited
        
            
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        f = k % len(nums)
        if f == 0:
            pass
        else:
            min_visited = self._rotate(nums,f,0)
            if min_visited != 1:
                for i in range(1,min_visited):
                    self._rotate(nums,f,i)
            
                
            
        
