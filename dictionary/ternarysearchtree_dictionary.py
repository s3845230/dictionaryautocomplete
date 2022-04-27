from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    root_node = Node()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for current_word in words_frequencies:
            self.add_word_frequency(current_word)

        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

    def search(self, word: str) -> int:
        letterCount = 0
        tracked_node = self.root_node
        for current_letter in word:
                letterCount+=1
                nextLetter = False
                while not nextLetter:
                    if (tracked_node.letter is None):
                        tracked_node.letter = current_letter
                    # if letter matches, go down the tree
                    if(current_letter == tracked_node.letter):
                        # if on final letter, and in the correct node, set frequency and end_word
                        if (letterCount == len(word)):
                            if (tracked_node.end_word):
                                return tracked_node.frequency
                        elif (tracked_node.middle is None):
                            return 0
                        tracked_node = tracked_node.middle
                        nextLetter = True
                    # if letter is earlier in alphabet than current node letter
                    elif(ord(current_letter) < ord(tracked_node.letter)):
                        if (tracked_node.left is None):
                            return 0
                        # if letter is alphabetically further than the left node
                        if(ord(current_letter) <= ord(tracked_node.left.letter)):
                            tracked_node = tracked_node.left
                        else:
                            return 0
                    # if letter is later in alphabet than current node letter
                    elif(ord(current_letter) > ord(tracked_node.letter)):
                        if (tracked_node.right is None):
                            return 0
                        # if letter is alphabetically further than the right node
                        if(ord(current_letter) >= ord(tracked_node.right.letter)):
                            tracked_node = tracked_node.right
                        else:
                            return 0
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        letterCount = 0
        tracked_node = self.root_node
        for current_letter in word_frequency.word:
                letterCount+=1
                nextLetter = False
                while not nextLetter:
                    if (tracked_node.letter is None):
                        tracked_node.letter = current_letter
                    # if letter matches, go down the tree
                    if(current_letter == tracked_node.letter):
                        # if on final letter, and in the correct node, set frequency and end_word
                        if (letterCount == len(word_frequency.word)):
                            if (tracked_node.end_word == True):
                                return False
                            else:
                                tracked_node.end_word = True
                                tracked_node.frequency = word_frequency.frequency
                                return True
                        elif (tracked_node.middle is None):
                            tracked_node.middle = Node()
                        tracked_node = tracked_node.middle
                        nextLetter = True
                    # if letter is earlier in alphabet than current node letter
                    elif(ord(current_letter) < ord(tracked_node.letter)):
                        if (tracked_node.left is None):
                            tracked_node.left = Node(current_letter)
                            tracked_node = tracked_node.left
                        # if letter is alphabetically further than the left node
                        elif(ord(current_letter) <= ord(tracked_node.left.letter)):
                            tracked_node = tracked_node.left
                        else:
                            # create new node, enter it
                            new_node = Node(current_letter)
                            old_left_node = tracked_node.left
                            # fixing references
                            old_left_node.right = new_node
                            new_node.left = old_left_node
                            new_node.right = tracked_node
                            tracked_node.left = new_node
                            tracked_node = new_node
                    # if letter is later in alphabet than current node letter
                    elif(ord(current_letter) > ord(tracked_node.letter)):
                        if (tracked_node.right is None):
                            tracked_node.right = Node(current_letter)
                            tracked_node = tracked_node.right
                        # if letter is alphabetically further than the right node
                        elif(ord(current_letter) >= ord(tracked_node.right.letter)):
                            tracked_node = tracked_node.right
                        else:
                            # create new node, enter it
                            new_node = Node(current_letter)
                            old_right_node = tracked_node.right
                            # fixing references
                            old_right_node.left = new_node
                            new_node.right = old_right_node
                            new_node.left = tracked_node
                            tracked_node.right = new_node
                            tracked_node = new_node
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        letterCount = 0
        tracked_node = self.root_node
        for current_letter in word:
                letterCount+=1
                nextLetter = False
                while not nextLetter:
                    if (tracked_node.letter is None):
                        tracked_node.letter = current_letter
                    # if letter matches, go down the tree
                    if(current_letter == tracked_node.letter):
                        # if on final letter, and in the correct node, set frequency and end_word
                        if (letterCount == len(word)):
                            if (tracked_node.end_word):
                                tracked_node.frequency = None
                                tracked_node.end_word = None
                                return True
                        elif (tracked_node.middle is None):
                            return False
                        tracked_node = tracked_node.middle
                        nextLetter = True
                    # if letter is earlier in alphabet than current node letter
                    elif(ord(current_letter) < ord(tracked_node.letter)):
                        if (tracked_node.left is None):
                            return False
                        # if letter is alphabetically further than the left node
                        if(ord(current_letter) <= ord(tracked_node.left.letter)):
                            tracked_node = tracked_node.left
                        else:
                            return False
                    # if letter is later in alphabet than current node letter
                    elif(ord(current_letter) > ord(tracked_node.letter)):
                        if (tracked_node.right is None):
                            return False
                        # if letter is alphabetically further than the right node
                        if(ord(current_letter) >= ord(tracked_node.right.letter)):
                            tracked_node = tracked_node.right
                        else:
                            return False
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        def recursive_search(current_prefix: str, current_node: Node, direction: int) -> [WordFrequency]:
            word_frequencies = []
            if (current_node.frequency is not None):
                current_word = WordFrequency(current_prefix + current_node.letter,current_node.frequency)
                # print(current_word.frequency)
                # print(current_word.word)
                # print("word name: " + current_word.word + ", frequency: " + str(current_word.frequency))
                word_frequencies.append(current_word)
                # print(word_frequencies[len(word_frequencies)-1].word)
            # if (current_node.middle is not None):
            #     word_frequencies.extend(recursive_search(current_prefix + current_node.letter, current_node.middle, 2))
            # if (current_node.left is not None and (direction == 1 or direction == 2)):
            #     word_frequencies.extend(recursive_search(current_prefix, current_node.left, 1))
            # if (current_node.right is not None and (direction == 3 or direction == 2)):
            #     word_frequencies.extend(recursive_search(current_prefix, current_node.right, 3))
            if (current_node.middle is not None):
                word_frequencies = word_frequencies + recursive_search(current_prefix + current_node.letter, current_node.middle, 2)
            if (current_node.left is not None and (direction == 1 or direction == 2)):
                word_frequencies = word_frequencies + recursive_search(current_prefix, current_node.left, 1)
            if (current_node.right is not None and (direction == 3 or direction == 2)):
                word_frequencies = word_frequencies + recursive_search(current_prefix, current_node.right, 3)
            return word_frequencies

        def find_best_three(all_suggestions: [WordFrequency]) -> [WordFrequency]:
            best_three = [None, None, None]
            for suggestion in all_suggestions:
                # print(suggestion.word)
                # print(suggestion.frequency)
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
            # for record in res:
            #     print(record)
            return res

        
        letterCount = 0
        tracked_node = self.root_node
        for current_letter in word:
                letterCount+=1
                nextLetter = False
                while not nextLetter:
                    if (tracked_node.letter is None):
                        tracked_node.letter = current_letter
                    # if letter matches, go down the tree
                    if(current_letter == tracked_node.letter):
                        # if on final letter, and in the correct node, set frequency and end_word
                        if (letterCount == len(word)):
                            # print(word)
                            if (tracked_node.middle is not None):
                                all_suggestions = recursive_search(word, tracked_node.middle, 2)
                                answer = find_best_three(all_suggestions)
                                return answer
                        elif (tracked_node.middle is None):
                            return []
                        tracked_node = tracked_node.middle
                        nextLetter = True
                    # if letter is earlier in alphabet than current node letter
                    elif(ord(current_letter) < ord(tracked_node.letter)):
                        if (tracked_node.left is None):
                            return []
                        # if letter is alphabetically further than the left node
                        if(ord(current_letter) <= ord(tracked_node.left.letter)):
                            tracked_node = tracked_node.left
                        else:
                            return []
                    # if letter is later in alphabet than current node letter
                    elif(ord(current_letter) > ord(tracked_node.letter)):
                        if (tracked_node.right is None):
                            return []
                        # if letter is alphabetically further than the right node
                        if(ord(current_letter) >= ord(tracked_node.right.letter)):
                            tracked_node = tracked_node.right
                        else:
                            return []
        # TO BE IMPLEMENTED
        # place holder for return
        return []
