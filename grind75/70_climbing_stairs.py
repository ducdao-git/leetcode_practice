class Solution:
    def climbStairs(self, n: int) -> int:
        db = [0] * (n + 2)  # n + 2 just in case n=1, then db[2] will be invalid
        db[1] = 1
        db[2] = 2

        for i in range(3, n + 1):
            db[i] = db[i - 1] + db[i - 2]

        return db[n]
