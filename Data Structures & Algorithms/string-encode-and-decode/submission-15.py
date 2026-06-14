class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        sizes, res = [], []

        for s in strs:
           sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(",")
        res.append("#")
        res.extend(strs)
        return ''.join(res)
    

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        list_to_return, sizes = [], []

        i = 0
        while s[i] != "#":
            sz = ""
            j = i
            while s[j] != ",":
                sz += s[j]
                j += 1
            
            sizes.append(int(sz))
            i = j + 1

        # move from the last comma to the first character of the string
        i += 1
        for size in sizes:
            list_to_return.append(s[i: i+size])
            i += size


        return list_to_return

            