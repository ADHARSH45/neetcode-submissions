class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum,max_sum = 0,nums[0]
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + nums[i]
            max_sum = max(max_sum,curr_sum)

        return max_sum
        