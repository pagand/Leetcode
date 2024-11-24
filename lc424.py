class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) ==0:
            return 0
        l = 0
        res = 1
        charmap = {}
        for r in range(len(s)):
            charmap[s[r]] = charmap.get(s[r],0)+1
            # maxc = 1
            # for c in charmap:
            #     if charmap[c]>maxc:
            #         maxc = charmap[c]
            maxc = max(charmap.values())
            if r-l+1-maxc>k:
                charmap[s[l]] -=1
                l +=1
            else:
                res = max(res, r-l+1)
        return res




if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 0)) # expected 1