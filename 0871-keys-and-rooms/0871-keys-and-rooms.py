class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for rm in rooms[room]:
                if rm not in visited:
                    dfs(rm) 
        dfs(0)
        return len(visited) == len(rooms)