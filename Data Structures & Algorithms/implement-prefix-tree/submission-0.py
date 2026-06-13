class Node: 
    def __init__(self):
        self.children = {}
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = Node()
            currentNode = currentNode.children[char]
        currentNode.word = True


    def search(self, word: str) -> bool:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]

        return currentNode.word
        

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]

        return True
        