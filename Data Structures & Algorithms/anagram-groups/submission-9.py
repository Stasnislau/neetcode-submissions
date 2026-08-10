from collections import defaultdict
import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            groups["#".join([str(cnt) for cnt in count])].append(s)
        return list(groups.values())