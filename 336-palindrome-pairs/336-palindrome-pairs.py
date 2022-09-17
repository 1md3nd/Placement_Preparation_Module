class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        word_indexes = { word: word_index for word_index, word in enumerate(words) }
        
        for word_index, word in enumerate(words):
            for index in range(len(word) + 1):
                prefix = word[:index]
                suffix = word[index:]
                
                if prefix == prefix[::-1]:
                    reversed_word = suffix[::-1]
                    if word != reversed_word and reversed_word in word_indexes:
                        pairs.append([word_indexes[reversed_word], word_index])
                
                if index != len(word) and suffix == suffix[::-1]:
                    reversed_word = prefix[::-1]
                    if word != reversed_word and reversed_word in word_indexes:
                        pairs.append([word_index, word_indexes[reversed_word]])
        
        return pairs