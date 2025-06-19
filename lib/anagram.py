# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        return [w for w in word_list if sorted(w.lower()) == sorted_word and w.lower() != self.word]

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  
