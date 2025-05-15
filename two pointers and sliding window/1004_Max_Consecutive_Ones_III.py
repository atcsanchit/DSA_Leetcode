class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        flip = k
        maxi = -1
        while end < len(nums):
            i = nums[end]
            if i == 0 and flip == 0:
                maxi = max(maxi,end-start)
                print(maxi)
                while start <= end and nums[start] != 0:
                    start += 1
                start += 1
            elif i == 0 and flip > 0:
                flip -= 1
            end += 1
        
        maxi = max(maxi,end-start)

        return maxi