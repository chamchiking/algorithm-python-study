class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text_list = text.split()
        text_list.sort(key=lambda x: len(x))
        answer = text_list[0][0].upper() + text_list[0][1:] + " "
        for i, t in enumerate(text_list):
            if i != 0:
                answer += t + " "
        return answer.rstrip()
