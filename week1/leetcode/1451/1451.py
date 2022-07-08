class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        split_text = text.lower().split(" ")
        sort_text = sorted(split_text, key=lambda x: len(x))
        join_text = " ".join(sort_text)
        join_text = join_text.capitalize()
        return join_text