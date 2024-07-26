class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        arr = title.split()
        for i in range(len(arr)):
            if len(arr[i]) <= 2:
                continue
            else:
                arr[i] = arr[i][0].upper() + arr[i][1:]
        return ' '.join(arr)