class Solution:
    def minOperations(self, n: int) -> int:
        # arr = []
        # counter = 1

        # for i in range(n):
        #     arr.append(counter)
        #     counter += 2
        
        # if len(arr) % 2 == 1:
        #     target = arr[len(arr) // 2]
        # else:
        #     target = arr[len(arr) // 2] + 1
        
        # total_diff = 0
        # for i in range(len(arr)):
        #     total_diff += abs(target - arr[i])

        # return total_diff // 2

        # the target is n, n is always the median of the array
        target = n
        total_diff = 0
        for i in range(n // 2):
            total_diff += target - (2 * i + 1)
        return total_diff