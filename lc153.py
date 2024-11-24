class Solution:
    def findMin(self, nums: list[int]) -> int:
        L, R= 0, len(nums)-1
        if nums[L]<nums[R]:
            return nums[L]
        while R-L>1:
            m = L+int((R-L)/2)
            if nums[m]>=nums[L]:
                L = m
            else:
                R = m
        return nums[R]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,1,2])) # expected 1