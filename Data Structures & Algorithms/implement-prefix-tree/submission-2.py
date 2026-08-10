import string

class PrefixNode:
    def __init__(self, letter = None, val = None, endOfWord = False):
        self.nxt = [None] * 26
        self.endOfWord = endOfWord
        if letter and val:
            index = getLetPos(letter)
            self.nxt[index] = val


def getLetPos(letter):
    return ord(letter) - ord('a')

class TrieNode:
    def __init__(self):
        # Используем словарь. Это удобнее, чем [None]*26.
        # Нет возни с ord(c) - ord('a').
        self.children = {} 
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # Если буквы нет — создаем тупик и идем в него
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # В конце помечаем флагом
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # Если пути нет — сразу False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Дошли до конца. Это конец слова или просто префикс?
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Если дошли и не упали — значит префикс есть.
        return True