class Node: 
    def __init__(self):
        self.children = {}
        self.word = False

    def nodeSearch(self, word) -> bool:
        currentNode = self
        substring = ''
        for char in word:
            substring += char
            if char == '.':
                subWord = word.split(substring, 1)[1]
                print(f"Subword is {subWord}")
                for node in currentNode.children:
                    if (currentNode.children[node].nodeSearch(subWord)):
                        return True
                return False
            elif char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        return currentNode.word
        

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = Node()
            currentNode = currentNode.children[char]
        currentNode.word = True

        

    def search(self, word: str) -> bool:
        return self.root.nodeSearch(word)
    
