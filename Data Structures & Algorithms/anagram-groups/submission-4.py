def ordString(string: str) -> int:
    count = 0
    for letter in string: 
        count += ord(letter) 
    return count


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        supportHash = {}

        for word in strs:
            wordCounter = [0] * 26
            for letter in word: 
                wordCounter[ord(letter) - ord('a')] += 1
            key = tuple(wordCounter)
            if key in supportHash:
                supportHash[key].append(word)
            else:
                supportHash[key] = [word]

        return list(supportHash.values())