class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        answer = [0] * N
        answer[0] = 1 if 0 < int(s[0]) <= 26 else 0

        for i in range(1, N):
            print(s[i], s[i - 1 : i + 1])
            if 0 < int(s[i]) <= 26:
                answer[i] += answer[i - 1]
            if 0 < int(s[i - 1 : i + 1]) <= 26 and s[i - 1] != "0":
                answer[i] += answer[i - 2] if i - 2 >= 0 else 1
        return answer[-1]
