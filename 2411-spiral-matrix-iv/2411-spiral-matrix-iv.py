# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        # directions order should be right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        arr = [[-1] * n for _ in range(m)]
        cache = set()
        target = m * n
        row, col = 0, 0
        rows, cols = m, n
        direction = 0


        while head:
            arr[row][col] = head.val
            head = head.next
            cache.add((row, col))
            dx, dy = directions[direction % 4]
            if not (0 <= row + dx < rows and 0 <= col + dy < cols) or ((row + dx, col + dy) in cache): 
                direction += 1
                dx, dy = directions[direction % 4]
            
            row += dx
            col += dy
        
        return arr

        