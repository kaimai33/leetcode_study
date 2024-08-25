class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        ans = []
        def dfs(curr_node, path):
            path.append(curr_node)
            if curr_node == end:
                ans.append(path.copy())
                return
            
            for i in range(len(graph[curr_node])):
                dfs(graph[curr_node][i], path.copy())
        
        dfs(0, [])
        return ans
        