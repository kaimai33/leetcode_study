class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            discovered.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in discovered:
                    dfs(neighbor)

        discovered = set()
        adj_list = defaultdict(list)
        ans = 0
        curr_set = set()
        n = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        
        for i in range(n):
            if i not in discovered:
                dfs(i)
                ans += 1

        return ans
            

        



        