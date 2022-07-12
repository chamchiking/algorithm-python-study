# list[0] > list[1] < list[2] > list[3] ***
# list[0] < list[1] > list[2] < list[3] ***
# 두 경우를 보면서 문제가 되는 지점을 뽑아본 뒤

# 실패

# i - 1 > i < i + 1를 조건으로 만족하도록 i값을 수정하도록 하면 되려나?

class Solution:
    def movesToMakeZigzag(self, nums):
        # list[0] > list[1] < list[2] > list[3] ***
        # list[0] < list[1] > list[2] < list[3] ***
        # 두 경우의 수를 모두 구해서 최솟값 리턴
        case_1_moves = 0
        case_1_result = nums
        case_2_moves = 0
        case_2_result = nums
        
        for i in range(len(case_1_result)):
            if i < len(case_1_result) - 1:
                if i % 2 == 0:
                    print(i, ' >')
                    # list[i] > list[i+1]
                    diff = case_1_result[i+1] - case_1_result[i]
                    if diff >= 0: # list[i] <= list[i+1]
                        print(i, 'add diff')
                        case_1_result[i] += diff + 1
                        case_1_moves += diff + 1
                else:
                    print(i, ' <')
                    # list[i] < list[i+1]
                    diff = case_1_result[i+1] - case_1_result[i]
                    if diff <= 0: # list[i] >= list[i+1]
                        print(i, 'add diff')
                        case_1_result[i] += diff - 1
                        case_1_moves += (diff - 1) * -1
            else: # 마지막 경우
                if (len(case_1_result) - 1) % 2 == 0:
                    # list[i] < list[i+1]
                    print(len(case_1_result) -1, ' <')
                    diff = case_1_result[-1] - case_1_result[-2]
                    if diff <= 0:
                        print(i, 'add diff')
                        case_1_result[-1] += diff - 1
                        case_1_moves += (diff - 1) * -1
                else:
                    # list[i] > list[i+1]
                    print(len(case_1_result) -1, ' >')
                    diff = case_1_result[-1] - case_1_result[-2]
                    if diff >= 0:
                        print(i, 'add diff')
                        case_1_result[-1] += diff + 1
                        case_1_moves += diff + 1
                    
            print("case_1_result: ", case_1_result)
        
        for i in range(len(case_2_result)):
            if i < len(case_2_result) - 1:
                if i % 2 == 1:
                    print(i, ' >')
                    # list[i] > list[i+1]
                    diff = case_2_result[i+1] - case_2_result[i]
                    if diff >= 0: # list[i] <= list[i+1]
                        print(i, 'add diff')
                        case_2_result[i] += diff + 1
                        case_2_moves += diff + 1
                else:
                    print(i, ' <')
                    # list[i] < list[i+1]
                    diff = case_2_result[i+1] - case_2_result[i]
                    if diff <= 0: # list[i] >= list[i+1]
                        print(i, 'add diff')
                        case_2_result[i] += diff - 1
                        case_2_moves += (diff - 1) * -1
            else: # 마지막 경우
                if (len(case_2_result) - 1) % 2 == 1:
                    # list[i] < list[i+1]
                    print(len(case_2_result) -1, ' <')
                    diff = case_2_result[-1] - case_2_result[-2]
                    if diff <= 0:
                        print(i, 'add diff')
                        case_2_result[-1] += diff - 1
                        case_2_moves += (diff - 1) * -1
                else:
                    # list[i] > list[i+1]
                    print(len(case_2_result) -1, ' >')
                    diff = case_2_result[-1] - case_2_result[-2]
                    if diff >= 0:
                        print(i, 'add diff')
                        case_2_result[-1] += diff + 1
                        case_2_moves += diff + 1
                    
            print("case_2_result: ", case_2_result)

        print(case_1_moves)
        print(case_2_moves)

        return min(case_1_moves, case_2_moves)

s = Solution()
print(s.movesToMakeZigzag([9,6,1,6,2]))