class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            current = s[i]
            if current in dict_s.keys():
                dict_s[current] += 1
            else:
                dict_s[current] = 1

        for i in range(len(t)):
            current = t[i]
            if current in dict_t.keys():
                dict_t[current] += 1
            else:
                dict_t[current] = 1
            
        if len(dict_s.keys()) != len(dict_t.keys()):
            return False
        
        for key in dict_s.keys():
            if key not in dict_t.keys() or dict_s[key] != dict_t[key]:
                return False
            

        return True
        