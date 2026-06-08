class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        We can do this by sorting each string and then putting it in a hash table. All subsequent strings with the same letters will already exist in the table and we can add them to the result. We will map 'aet' -> ['tea','eat','ate'] and return all the values in a combined array at completion.
        '''
        ret : List[List[str]] = []

        map : dict[str: List[str]] = {}

        # sort and insert strings into appropriate table positions
        for s in strs:
            strSorted = ''.join(sorted(s))  # sort
            map[strSorted] = [s] if map.get(strSorted) is None else (map[strSorted] + [s])  # insert
        
        for key, value in map.items():
            ret.append(value)

        return ret