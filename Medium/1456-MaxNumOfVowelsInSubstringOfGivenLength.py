class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        # Count vowels in the first 'k' length substring
        vowel_count = sum(1 for ch in s[:k] if ch in vowels)
        max_vowels = vowel_count
        
        # For-loop to slide the window of k across the string
        for i in range(k, len(s)):
            
            # Remove leftmost char if it was a vowel
            if s[i-k] in vowels:
                vowel_count-=1
            
            # Add the rightmost char if it is a vowel
            if s[i] in vowels:
                vowel_count+=1

            max_vowels = max(max_vowels, vowel_count)

        return max_vowels
        





        
