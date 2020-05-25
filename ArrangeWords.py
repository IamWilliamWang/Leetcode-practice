class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        words = text.strip().split()
        result = ' '.join(sorted(words,key=lambda string:len(string)))
        result = result[0].upper() + result[1:]
        return result
