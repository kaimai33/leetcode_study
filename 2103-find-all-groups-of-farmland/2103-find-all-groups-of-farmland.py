class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # runs dfs at the top left coordinate, returns bottom right coordinate
        ans = []

        visited = set()
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1 and (i,j) not in visited:
                    r1 = i
                    c1 = j
                    r2 = r1
                    c2 = c1
                    for k in range(i, len(land)):
                        if land[k][j] == 1:
                            r2 = k
                        else:
                            break
                    for l in range(j, len(land[0])):
                        if land[i][l] == 1:
                            c2 = l
                        else:
                            break
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            visited.add((r, c))
                    ans.append([r1, c1, r2, c2])
        return ans

