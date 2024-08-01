class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            # collision case
            while ans and asteroid < 0 < ans[-1]:
                # asteroid is stronger
                if ans[-1] < -asteroid:
                    ans.pop()
                    continue
                # equal case
                elif ans[-1] == -asteroid:
                    ans.pop()
                break
            else:
                ans.append(asteroid)

        return ans

        