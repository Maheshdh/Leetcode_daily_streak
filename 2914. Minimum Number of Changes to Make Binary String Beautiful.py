# consider each sub-string of length 2
# if they are not the same, increment count by 1, since for larger sub-strings of even length, either of them should be converted. 
# jump by 2 in the loop

# Time Complexity -> O(N)
# Space Complexity -> O(1)
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                count += 1
        return count
        
