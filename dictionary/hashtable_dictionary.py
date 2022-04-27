from re import T
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):
    hashtable_dict = {}
    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for word in words_frequencies:
            self.add_word_frequency(word)
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

    def search(self, word: str) -> int:
        if self.hashtable_dict.get(word) is not None:
            return self.hashtable_dict.get(word)
        else:
            return 0
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        if self.hashtable_dict.get(word_frequency.word) is None:
            self.hashtable_dict[word_frequency.word] = word_frequency.frequency
            return True
        else:
            return False
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def delete_word(self, word: str) -> bool:
        if self.hashtable_dict.get(word) is not None:
            self.hashtable_dict.pop(word)
            return True
        else:
            return False
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        keys_list = self.hashtable_dict.keys()
        autocomplete_options = {}
        for key in keys_list:
            if (word == key[0:len(word)]):
                autocomplete_options[key] = self.hashtable_dict[key]
        best_keys = sorted(autocomplete_options, key=autocomplete_options.get, reverse=True)[:3]
        return_list = []
        for best_three in best_keys:
            return_list.append(WordFrequency(best_three, self.hashtable_dict[best_three]))
        return return_list
        

        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return []
