class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text_list = text.split()
        text_list.sort(key=len)
        string = ''
        for i, t in enumerate(text_list):
            if i ==0:
                string = t
            else:
                string = string+ ' ' + t
        answer = string.capitalize()
        return answer
