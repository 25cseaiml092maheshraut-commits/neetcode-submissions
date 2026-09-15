class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store numbers
        
        for num in nums:
            if num in seen:
                return True  # We found a duplicate!
            seen.add(num)    # Save this number for later checks
            
        return False  # No duplicates found