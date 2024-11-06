class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cur_min, cur_max = nums[0],nums[0]
        prev_max = -float('inf')
        for n in nums:
            if self.count_set_bits(n) == self.count_set_bits(cur_min):
                cur_min = min(cur_min,n)
                cur_max = max(cur_max,n)
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min , cur_max = n , n
        if cur_min < prev_max:
            return False
        return True
    
    def count_set_bits(self,n):
        print("n = ",n)
        count = 0
        while n:
            count += (n & 1)
            n = n >> 1
        print("set bits ",count)
        return count

        
        
