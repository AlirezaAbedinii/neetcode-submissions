class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        
        current['*'] =  True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current:
                return False
            else:
                current = current[char]
        
        if '*' in current and current['*']:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            else:
                current = current[char]
        
        return True