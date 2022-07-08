class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # zigzag array를 생성하는 2가지 방법
            # 1. A[0]이 더 큰 경우 - even
            # 2. A[0]이 더 작은 경우 - odd
        zig, zag = 0, 0
        # zig = increasing (even-indexed element greater than adjacents)
        # zag = decreasing (odd-indexed element greater than adjacents)
        prev_zig, prev_zag = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            # even index
            if i % 2 == 0:
                zig += max(0, prev_zig - nums[i]+1)
                prev_zig = nums[i]
                zag += max(0, nums[i] - prev_zag+1)
                prev_zag = nums[i] - max(0, nums[i] - prev_zag+1)
            # odd index
            else:
                zag += max(0, prev_zag - nums[i]+1)
                prev_zag = nums[i]
                zig += max(0, nums[i] - prev_zig+1)
                prev_zig = nums[i] - max(0, nums[i] - prev_zig+1)
        return min(zig, zag)