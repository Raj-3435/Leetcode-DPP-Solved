#Problem 2163: Minimum Difference in Sums After Removal of Elements


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        N3 = N // 3

        sum_left = sum_right = 0
        left = SortedList()
        right = SortedList()

        for i in range(N3):
            sum_left += nums[i]
            left.add(nums[i])

        
        for i in range(N3, N):
            sum_right += nums[i]
            right.add(nums[i])
        
       
        floating = SortedList()
        
       
        for _ in range(N3):
            x = right[0]
            right.remove(x)
            sum_right -= x

            floating.add(x)
        
       
        best = sum_left - sum_right

        for i in range(N3, 2 * N3):
            if nums[i] in right:
                right.remove(nums[i])
                sum_right -= nums[i]
                f = floating[-1]
                floating.remove(f)

                right.add(f)
                sum_right += f
            else:
                floating.remove(nums[i])
            
            left.add(nums[i])
            sum_left += nums[i]
            
            
            b1 = left[-1]
            left.remove(b1)
            sum_left -= b1

            best = min(best, sum_left - sum_right)
        return best