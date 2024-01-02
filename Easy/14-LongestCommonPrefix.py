class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # variable to return the response
        res = ""

        # sort the array elements alphabetically
        strs = sorted(strs)

        # after sorting, it can be assumed that the first and the last
        # elements can be used to find the longest prefix. 
        first = strs[0]
        last = strs[-1]

        # Iterate throigh each character of the two words until the shorter words
        # end is reached or the common prefix is found then return the prefix
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res+=first[i]
        return res
