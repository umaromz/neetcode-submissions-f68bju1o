from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dumbest solution
        sort_strs = []
        list_to_return = []
        my_dict = defaultdict(list)
        for i in range (len(strs)):
            sort_strs.append("".join(sorted(strs[i])))

        for i in range (len(sort_strs)):
            my_dict[sort_strs[i]].append(strs[i])        

        return list(my_dict.values())
        