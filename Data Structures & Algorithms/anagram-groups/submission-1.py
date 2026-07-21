class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for string in strs:
            key = ''.join(sorted(string))
            if key in groups.keys():
                groups[key].append(string)
            else:
                groups[key] = [string]
        return list(groups.values())
