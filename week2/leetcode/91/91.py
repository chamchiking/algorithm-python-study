import string
import itertools

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A ~ Z까지 매칭되는 딕셔너리 생성
        dict = {}
        num_lst = [i for  i in range(1, len(string.ascii_uppercase)+1)]
        j = 0
        for str in string.ascii_uppercase:
            dict[str] = num_lst[j]
            j += 1
        
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1,1
        
        # 1. 만들어지는 조합이 아무것도 없는 경우
        if s[0] == "0":
            return 0
        
        # 2. 조합이 만들어지는 경우
        for i in range(2, len(s)+1):
            # 2-1. 한 글자씩 보기
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            # 2-2. 두 글자씩 보기
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[-1]
        # 뒤에서부터 가장 마지막에 있는 원소 출력 dp[-1]