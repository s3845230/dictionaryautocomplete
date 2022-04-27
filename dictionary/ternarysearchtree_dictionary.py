from turtle import left
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

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        rootNode = Node()
        for currentWord in words_frequencies:
            trackedNode = rootNode
            seperatedWord = []
            seperatedWord[:0] = currentWord.word
            # for first word, constructed 'manually'. might adjust to only first letter are full code construction
                # for last letter, set frequency and endword boolean
                # trackedNode.frequency = currentWord.frequency
                # trackedNode.end_word = True
            for currentLetter in seperatedWord:

                nextLetter = False
                while not nextLetter:
                    if (trackedNode.letter is None):
                        trackedNode.letter = currentLetter
                    # if letter matches, go down the tree
                    if(currentLetter == trackedNode.letter):
                        if (trackedNode.middle is None):
                            trackedNode.middle = Node()
                        trackedNode = trackedNode.middle
                        nextLetter = True
                    # if letter is earlier in alphabet than current node letter
                    elif(ord(currentLetter) < ord(trackedNode.letter)):
                        if (trackedNode.left is None):
                            trackedNode.left = Node(currentLetter)
                            trackedNode = trackedNode.left
                        # if letter is alphabetically further than the left node
                        if(ord(currentLetter) <= ord(trackedNode.left.letter)):
                            trackedNode = trackedNode.left
                        else:
                            # create new node, enter it
                            newNode = Node(currentLetter)
                            oldLeftNode = trackedNode.left
                            # fixing references
                            oldLeftNode.right = newNode
                            newNode.left = oldLeftNode
                            newNode.right = trackedNode
                            trackedNode.left = newNode
                            trackedNode = newNode
                    # if letter is later in alphabet than current node letter
                    elif(ord(currentLetter) > ord(trackedNode.letter)):
                        if (trackedNode.right is None):
                            trackedNode.right = Node(currentLetter)
                            trackedNode = trackedNode.right
                        # if letter is alphabetically further than the right node
                        if(ord(currentLetter) >= ord(trackedNode.right.currentLetter)):
                            trackedNode = trackedNode.right
                        else:
                            # create new node, enter it
                            newNode = Node(currentLetter)
                            oldRightNode = trackedNode.right
                            # fixing references
                            oldRightNode.left = newNode
                            newNode.right = oldRightNode
                            newNode.left = trackedNode
                            trackedNode.right = newNode
                            trackedNode = newNode

        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return []
