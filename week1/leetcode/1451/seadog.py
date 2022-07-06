class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        
        words = text.split(' ')

        words_with_len = []
        for i in range(len(words)):
            words_with_len.append([words[i], i])

        words_with_len.sort(key=lambda x : (len(x[0]), x[1]))

        answer = ' '.join([ x[0] for x in words_with_len ])
        answer = answer[0].upper() + answer[1:]
        return answer