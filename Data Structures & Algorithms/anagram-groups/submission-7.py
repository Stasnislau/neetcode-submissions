from collections import defaultdict
import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            resultStr = self.getWordString(s)
            groups[resultStr].append(s)
        print(groups)
        return list(groups.values())


    def getWordString(self, s: str) -> str:
        alph = dict.fromkeys(string.ascii_lowercase, 0);
        for c in s:
            alph[c] += 1
        return "".join([f"{char}{count}" for char, count in alph.items() if count != 0])