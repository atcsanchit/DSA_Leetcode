class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        a = None
        b = None
        mapping = {}
        maxi = -1
        while end < len(fruits):

            if a == None:
                a = fruits[end]
                mapping[fruits[end]] = 1
            elif a != None and b == None and fruits[end] != a:
                b = fruits[end]
                mapping[fruits[end]] = 1
            elif fruits[end] in [a,b]:
                mapping[fruits[end]] = mapping.get(fruits[end], 0) + 1
            elif a != None and b != None and fruits[end] != a and fruits[end] != b:
                maxi = max(maxi,end-start)
                
                prev = fruits[end-1]
                look_for = a if prev == b else b
                while start < end and mapping[look_for] > 0:
                    if fruits[start] == look_for:

                        mapping[look_for] -= 1

                    elif mapping[fruits[start]] > 0:
                        mapping[fruits[start]] -= 1   
                    start += 1
                
                mapping[fruits[end]] = 1

                if a == look_for:
                    a = fruits[end]
                else:
                    b = fruits[end]
            
            end += 1

        maxi = max(maxi,end-start)

        return maxi