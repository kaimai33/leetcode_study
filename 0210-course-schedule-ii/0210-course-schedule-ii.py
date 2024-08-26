class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list) # each node in the dictionary is automatically assigned an empty list
        in_degree = {i: 0 for i in range(numCourses)}

        for dest, src in prerequisites:
            adjlist[src].append(dest)
            in_degree[dest] += 1

        queue = deque([node for node in in_degree if in_degree[node] == 0])

        count = 0
        ans = []

        while len(queue) > 0:
            node = queue.popleft()
            ans.append(node)
            count += 1

            for neighbor in adjlist[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if count == numCourses:
            return ans
        else:
            return []