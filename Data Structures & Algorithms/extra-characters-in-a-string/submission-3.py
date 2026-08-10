from functools import cache
class Node:
    def __init__(self, key = None, val = None):
        self.children = {}
        self.end = False
        if key and val:
            self.children[key] = val
    
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.root = Node(self)

        def add_word(word):
            chars = list(word)
            curr = self.root
            for c in chars:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
            curr.end = True

        for word in dictionary:
            add_word(word)
            
        @cache
        def make_choice(i):
            if i == len(s):
                return 0
            missing = make_choice(i+1) + 1
            curr = self.root
            while i < len(s):
                c = s[i]
                if c not in curr.children:
                    break
                curr = curr.children[c]
                if curr.end:
                    missing = min(missing, make_choice(i+1))
                i += 1
            return missing



        return make_choice(0)

                

