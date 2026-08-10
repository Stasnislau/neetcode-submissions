class Node:
    def __init__(self, key = None, val = None):
        self.isEndOfWord = False
        self.children = {}
        if key and val:
            self.children[key] = val
class Tree:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word, starting_node):
        curr = starting_node if starting_node else self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr if curr != starting_node else None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Tree()
        result = set()
        def backtrack(x, y, word, curr_node):
            if not curr_node:
                return None
            if curr_node.isEndOfWord:
                result.add("".join(word))
            if x < 0 or x >= x_max or y < 0 or y >= y_max:
                return None
            temp_node = tree.search(board[y][x], curr_node)
            if not temp_node:
                return 
            word.append(board[y][x])
            temp = board[y][x]
            board[y][x] = '#'
            backtrack(x + 1, y, word, temp_node)
            backtrack(x - 1, y, word, temp_node)
            backtrack(x, y - 1, word, temp_node)
            backtrack(x, y + 1, word, temp_node)
            word.pop()
            board[y][x] = temp

        x_max = len(board[0])
        y_max = len(board)        
        for word in words:
            tree.add(word)

        for y in range(y_max):
            for x in range(x_max):
                backtrack(x,y, [], tree.root)
        
        return list(result)
        

  
        
