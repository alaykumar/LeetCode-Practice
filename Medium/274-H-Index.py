from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citation list in descending order
        citations.sort(reverse=True)

        # Iterate over the sorted list
        for i, citation in enumerate(citations):
            # If the current citation count is less than the position (h-index condition)
            if citation < i + 1:
                return i  # Return the highest valid h-index
        
        # If all citations meet the h-index condition, return the total number of papers
        return len(citations)
