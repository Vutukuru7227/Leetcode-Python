#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
#Specifically, ans is the concatenation of two nums arrays.
#
#Return the array ans.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,1]
#Output: [1,2,1,1,2,1]
#Explanation: The array ans is formed as follows:
#- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
#- ans = [1,2,1,1,2,1]
#Example 2:
#
#Input: nums = [1,3,2,1]
#Output: [1,3,2,1,1,3,2,1]
#Explanation: The array ans is formed as follows:
#- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
#- ans = [1,3,2,1,1,3,2,1]
# 
#
#Constraints:
#
#n == nums.length
#1 <= n <= 1000
#1 <= nums[i] <= 1000

## The below solution is a modified version where we can concatenate based on the multiplier (can be 2 or more)

class Solution:
    def getConcatenation(self, nums: list[int],multiplier) -> list[int]:
        ans = []
        for i in range (multiplier):
            ans += nums
        return ans

def main():
    nums=[0,1,2]
    multiplier = 3
    soln = Solution()
    result = soln.getConcatenation(nums,multiplier)
    print (result)

if __name__ == "__main__":
    main()