# n까지의 경우의 수 = n-1까지의 경우의 수 + s[n]
# s[n]이 -가 되는 경우가 있는 거 같음

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        
        if s[0] != '0':
            dp[0] = 1

        print(dp[0])

        for i in range(1, len(s)):
            print(f"i: {i}")
            case = 0

            # # 앞이 0이 아니고 자기자신으로 경우가 되는지
            # if (i-1 < 0 or (i-1 >= 0 and s[i-1] != '0')) and s[i] != '0':
            #     print(s[i])
            #     case = case + 1

            # 앞자리랑 합쳐서 경우가 되는지
            if i-1 >= 0 and s[i-1] != '0' and s[i] != '0' and int(s[i-1:i+1]) < 27:
                print(s[i-1:i+1])
                case = case + 1
            
            if i > 0:
                dp[i] = dp[i - 1] + case
        
        answer = dp[len(s) - 1]
        return answer

s = Solution()
print(s.numDecodings("21"))