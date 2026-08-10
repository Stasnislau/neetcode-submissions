import string

class PrefixNode:
    def __init__(self, letter = None, val = None, endOfWord = False):
        self.let = letter
        self.nxt = [None] * 26
        self.endOfWord = endOfWord
        if letter and val:
            index = getLetPos(letter)
            self.nxt[index] = val


def getLetPos(letter):
    return ord(letter) - ord('a')

class PrefixTree:

    def __init__(self):
        nxt = [None] * 26
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        (node, lastIndex) = self._getLastNode(word)
        print('covered',lastIndex, ' elements', word)
        for i in range(lastIndex, len(word)):
            index = getLetPos(word[i])
            node.nxt[index] = PrefixNode(word[i])
            node = node.nxt[index]
            print('adding', word[i])
        node.endOfWord = True
        print('added', word, node.let, node.endOfWord)
        


    def _getLastNode(self, word: str):
        letters = list(word)
        curr = self.root
        lastIndex = -1
        for i, letter in enumerate(letters):
            index = getLetPos(letter)
            if curr.nxt[index]:
                curr = curr.nxt[index]
                lastIndex = i
            else:
                break
        return (curr, lastIndex + 1)



    def search(self, word: str) -> bool:
        (node, index) = self._getLastNode(word)
        return index == len(word) and node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        return self._getLastNode(prefix)[1] == len(prefix)
        
        