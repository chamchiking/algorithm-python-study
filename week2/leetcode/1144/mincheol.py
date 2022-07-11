import math

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        mov1 = 0
        mov2 = 0
        N = len(nums)
        for i, n in enumerate(nums):
            if i%2 ==0:
                left = nums[i-1] if i-1 >=0 else math.inf
                right = nums[i+1] if i+1 <N else math.inf
                minimum = min(left, right)
                if n >= minimum:
                    mov1 += n-minimum+1
            else:
                left = nums[i-1] if i-1 >=0 else math.inf
                right = nums[i+1] if i+1 <N else math.inf
                minimum = min(left, right)
                if n >= minimum:
                    mov2 += n-minimum+1
        return min(mov1, mov2)