class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointer approach
        start = 0
        end = 0
        maxi = -1
        while end < len(s):
            substr = s[start:end+1]
            end += 1

            if end < len(s) and s[end] in substr:
                maxi = max(maxi, end-start)
                while start < end and s[start] != s[end]:
                    start += 1
                start += 1
            

        print(end)
        print(start)
        maxi = max(maxi, end-start)
        return maxi
            
