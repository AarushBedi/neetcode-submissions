from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word, reverse=True))
            if word_sorted in word_dict:
                word_dict[word_sorted].append(word)
            else:
                word_dict[word_sorted].append(word)
        
        return list(word_dict.values())


