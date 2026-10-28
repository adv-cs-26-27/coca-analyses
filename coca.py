import matplotlib.pyplot as plt

# =================
# HELPER FUNCTIONS
# =================

### sorting dictionary by values, descending ###
def sort_dict_by_descending_values(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

##### TASK 1 #####
"""
Write a function that takes in a file name and returns a dictionary 
that maps each word in the text to the number of times that word 
appears in the text.

Be sure to "clean" each word, before adding it to the dictionary,
i.e. remove punctuation/numbers/whitespace, and convert it to lowercase.
You may want to make a helper function for this! 
"""

def create_word_count_dict(filename):
    pass


##### TASK 2 #####
"""
Write a function that takes in a dictionary of word counts as input 
(exactly like the output of create_word_count_dict()) and returns a 
dictionary of word frequencies. The word frequency of a word is the 
fraction of the total words that are that word, represented as a floating 
point number. 

For example, given the dictionary {"hello": 2, "world": 2, "hi": 1} as input, 
your function should return a dictionary {"hello": 0.4, "world": 0.4, "hi": 0.2}.
"""

def word_freq_dict(word_count_dict):
    pass


##### TASK 3 #####
"""
Write a function that takes in two word frequency dictionaries and generates 
a dictionary that describes the frequency of unique words in the first dictionary. 
Your output dictionary should contain words that only appear in the first 
dictionary as keys, and these words’ frequencies as the values.
"""

def unique_freqs(wfdict1, wfdict2):
    pass


##### TASK 4 #####
"""
Choose one of the COCA samples (academic, blog, fiction, magazine, news, spoken,
tv/movies, web).

Create a bar graph comparing the number of unique words for your chosen sample
when compared to each of the other samples.
"""

def unique_words_graph():
    pass


##### TASK 5 #####
"""
Create a bar graph comparing the number of words longer than 15 letters 
in each of the corpuses.
"""

def num_long_words_graph():
    pass

##### TASK 6 #####
"""
Your choice: use at least two of the COCA samples to create a new visualization
based on an attribute that you have not explored yet.
"""