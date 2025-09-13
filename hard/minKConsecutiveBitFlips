class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = 0  
        res = 0
        hint = [0] * n  

        for i in range(n):
            if i >= k:
                flip ^= hint[i - k]  

            if nums[i] ^ flip == 0:  
                if i + k > n:
                    return -1  
                hint[i] = 1
                flip ^= 1
                res += 1
        return res
