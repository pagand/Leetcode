class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while R-L>1:
            m = L + int((R-L)/2)
            if nums[m] > nums[L]:
                if target > nums[m]:
                    L = m
                else:
                    if target<nums[L]:
                        L = m
                    else:
                        R = m
            else:
                if target > nums[R]:
                    R = m
                else:
                    if target>nums[m]:
                        L= m
                    else:
                        R = m
        if target == nums[L]:
            return L
        elif target == nums[R]:
            return R
        else:
            return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0)) # expected 4