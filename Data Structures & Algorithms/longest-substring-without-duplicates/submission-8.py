class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i + 1
        if len(s) < 2:
            return len(s)
        maxLength = 1    
        currentCheck = set(s[i]) 
        while i < len(s):
            while j < len(s):
                if s[j] in currentCheck:
                    break;
                currentCheck.add(s[j])
                j += 1    
            maxLength = max(len(currentCheck), maxLength)
            currentCheck.discard(s[i])
            i += 1
        

        return maxLength




            

