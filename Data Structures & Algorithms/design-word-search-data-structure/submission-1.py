class Node:
    def __init__(self, key = None, val = None):
        self.children = {}
        self.endOfWord = False
        if key and val:
            self.children[key] = val

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        chars = list(word)
        curr = self.root
        for c in chars:
            if not curr.children.get(c):
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in node.children:
                        if dfs(i + 1, node.children[child]):
                            return True
                    
                    return False
                else: 
                    if c not in node.children:
                        return False
                    else:
                        node = node.children[c]
            return node.endOfWord

        return dfs(0, self.root)
                        


            
        
