from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

CHAR_ORD = 96
LIST_SIZE = 27
_dict = [None]*LIST_SIZE
_charIndex = [0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class ListDictionary(BaseDictionary):


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        word = word_frequency.word
        frequency = word_frequency.frequency
        indexChain = _dict

        for char in word:
            if indexChain[ord(char)-CHAR_ORD] == None:
                indexChain[ord(char)-CHAR_ORD] = [None]*LIST_SIZE
            indexChain = indexChain[ord(char)-CHAR_ORD]
        
        if indexChain[0] != None:
            return False
        else:
            indexChain[0] = frequency
            # print(_dict)
            return True

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        indexChain = _dict

        try:
            for char in word[:-1]:
                indexChain = indexChain[ord(char)-CHAR_ORD]

            if indexChain[ord(word[-1])-CHAR_ORD][0] != None:
                return indexChain[ord(word[-1])-CHAR_ORD][0]
            else:
                return 0
        except:
            return 0

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        indexChain = _dict

        try:
            for char in word[:-1]:
                indexChain = indexChain[ord(char)-CHAR_ORD]

            if indexChain[ord(word[-1])-CHAR_ORD][0] != None:
                indexChain[ord(word[-1])-CHAR_ORD][0] = None
                return True
            else:
                return False
        except:
            return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        indexChain = _dict
        words_frequencies = []

        def recursiveSearch(prefix_word, indexChain):

            for i in range(1, LIST_SIZE-1):

                if indexChain[i] != None:

                    if indexChain[i][0] != None:
                        word = WordFrequency((prefix_word + _charIndex[i]), indexChain[i][0])
                        words_frequencies.append(WordFrequency((prefix_word + _charIndex[i]), indexChain[i][0]))
                    
                    recursiveSearch(prefix_word + _charIndex[i], indexChain[i])
                else:
                    pass

        def find_best_three(words_frequencies: [WordFrequency]) -> [WordFrequency]:
            best_three = [None, None, None]
            for suggestion in words_frequencies:
                if (best_three[0] is None):
                    best_three[0] = suggestion
                elif (best_three[0].frequency < suggestion.frequency):
                    best_three[2] = best_three[1]
                    best_three[1] = best_three[0]
                    best_three[0] = suggestion
                elif (best_three[1] is None):
                    best_three[1] = suggestion
                elif (best_three[1].frequency < suggestion.frequency):
                    best_three[2] = best_three[1]
                    best_three[1] = suggestion
                elif (best_three[2] is None):
                    best_three[2] = suggestion
                elif (best_three[2].frequency < suggestion.frequency):
                    best_three[2] = suggestion
            res = []
            for val in best_three:
                if val != None :
                    res.append(val)
            return res


        try:
            for char in prefix_word[:-1]:
                indexChain = indexChain[ord(char)-CHAR_ORD]

            if indexChain[ord(prefix_word[-1])-CHAR_ORD] is not None:
                indexChain = indexChain[ord(prefix_word[-1])-CHAR_ORD]
                recursiveSearch(prefix_word, indexChain)
        except:
            pass
                    
        return find_best_three(words_frequencies)
