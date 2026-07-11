class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i, val in enumerate(operations):
            try:
                res.append(int(val))
            except ValueError:
                if val == '+':
                    n = len(res) - 1
                    x = res[n - 1] + res[n]
                    res.append(x)
                elif val == 'D':
                    n = len(res) - 1
                    x = res[n] * 2
                    res.append(x)
                elif val == 'C':
                    res.pop()
                else:
                    return
        return sum(res)