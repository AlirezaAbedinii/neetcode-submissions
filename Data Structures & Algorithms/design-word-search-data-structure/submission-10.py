class WordDictionary:

    def __init__(self):
        self.root = {}        

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            current = current.setdefault(char, {})
        
        current['*'] = True

    def search(self, word: str) -> bool:
        current = self.root
        
        try:
            for char in word:
                if char not in current:
                    if char != '.':
                        return False
                    else:
                        values = list(current.values())
                        merged = {}
                        for i in range(len(values)):
                            if values[i] == True:
                                continue
                            
                            merged = merged | values[i]
                        current = merged
                else:
                    current = current[char]
            
            
               
            return '*' in current
        except Exception as e:
            return False
        return False