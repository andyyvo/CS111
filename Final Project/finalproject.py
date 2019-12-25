#
# finalproject.py - Final Project
#
# Part I: Building a initial text model

# 3
def clean_text(txt):
    """takes a string of text txt and returns a list containing the words
    in txt after it has been “cleaned”"""
    txt = txt.strip().lower()
    for i in '.,?!@#$%^&*()+-=':
        txt = txt.replace(i, '')
    return txt.split()

# 1

class TextModel:

    def __init__(self, model_name):
        """that constructs a new TextModel object by accepting a string
        model_name as a parameter and initializing name, words, word length
        frequency, stem frequency, sentence_length frequency and our choice"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.conjunctions = {'for': 0.5, 'and': 0.5, 'nor': 0.5, 'but': 0.5, 'or': 0.5, 'yet': 0.5, 'so': 0.5} # our choice

# 2
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of word stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of conjunctions: ' + str(len(self.conjunctions))
        return s
        
# 4
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model."""
        new_s = clean_text(s)
        word_list = new_s
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
        for w in word_list:
            if stems(w) not in self.stems:
                self.stems[stems(w)] = 1
            else:
                self.stems[stems(w)] += 1
        s = s.replace('?', '.')
        s = s.replace('!', '.')
        z = s.split('.')
        for i in z:
            sentence_word = i.split()
            sentence_len = len(sentence_word)
            if sentence_len not in self.sentence_lengths and sentence_len > 0:
                self.sentence_lengths[sentence_len] = 1
            elif sentence_len < 0:
                self.sentence_lengths[sentence_len] += 1
        for w in word_list:
            if w in ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']:
                if w not in self.conjunctions:
                    self.conjunctions[w] = 1
                else:
                    self.conjunctions[w] += 1

# 5
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        text = file.read()
        file.close()
        self.add_string(text)

# 1, part II
    def save_model(self):
        """saves the TextModel object self by writing its various feature dictionaries
        to files"""
 
        filename = self.name + '_words'
        d = self.words
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

        filename = self.name + '_word_lengths'
        d1 = self.word_lengths
        f = open(filename, 'w')
        f.write(str(d1))
        f.close()

        filename = self.name + '_stems'
        d2 = self.stems
        f = open(filename, 'w')
        f.write(str(d2))
        f.close()

        filename = self.name + '_sentence_lengths'
        d3 = self.sentence_lengths
        f = open(filename, 'w')
        f.write(str(d3))
        f.close()
        
        filename = self.name + '_conjunctions'
        d4 = self.conjunctions
        f = open(filename, 'w')
        f.write(str(d4))
        f.close()
        
# 2, part II
    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from
        their files and assigns them to the attributes of the called TextModel"""
        filename = self.name + '_words'
        f = open(filename, 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()
        
        d = dict(eval(d_str))      # Convert the string to a dictionary.
        self.words = d

        filename1 = self.name + '_word_lengths'
        f = open(filename1, 'r')    # Open for reading.
        d1_str = f.read()           # Read in a string that represents a dict.
        f.close()
        
        d1 = dict(eval(d1_str))      # Convert the string to a dictionary.
        self.word_lengths = d1

        filename2 = self.name + '_stems'
        f = open(filename2, 'r')    # Open for reading.
        d2_str = f.read()           # Read in a string that represents a dict.
        f.close()
        
        d2 = dict(eval(d2_str))      # Convert the string to a dictionary.
        self.stems = d2

        filename3 = self.name + '_sentence_lengths'
        f = open(filename3, 'r')    # Open for reading.
        d3_str = f.read()           # Read in a string that represents a dict.
        f.close()
        
        d3 = dict(eval(d3_str))      # Convert the string to a dictionary.
        self.sentence_lengths = d3

        filename4 = self.name + '_conjunctions'
        f = open(filename4, 'r')    # Open for reading.
        d4_str = f.read()           # Read in a string that represents a dict.
        f.close()
        
        d4 = dict(eval(d4_str))      # Convert the string to a dictionary.
        self.conjunctions = d4

# 2, Part 4

    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring the
        similarity of self and other"""
        words_score = compare_dictionaries(other.words, self.words)
        word_length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        conjunctions_score = compare_dictionaries(other.conjunctions, self.conjunctions)
        lst = [words_score, word_length_score, stems_score, sentence_lengths_score, conjunctions_score]
        return lst
    
# 3, Part 4
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source”
        TextModel objects and determines which of these other TextModels is
        the more likely source of the called TextModel"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))
        n1 = 0
        n2 = 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                n1 += 1
            else:
                n2 += 1
        if n1 > n2:
            print(self.name + ' is more likely to have come from '+  source1.name)
        else:
            print(self.name + ' is more likely to have come from '+  source2.name)
        
# Part II: Saving and retrieving a text model

def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

# Part 3: adding features to the model

def stems(s):
    """ Returns the 'stem' of 's', where the stem of a word is the root part
        of the word, which excludes and prefixes and suffixes.
        """
    s = s.lower()
    
    # verbs ending in 's' vs 'ss' (ex: plays vs. kiss(es)) # plural
    if s[-1] == 's':
        if len(s) < 2:
            return s
        elif s[-2] == 's':
            return s
        else:
            s = s[:-1]
            if len(s) < 3 or s == 'ship': # for words like ages and ships and ants and pies
                return s
            elif s[-1] == 'e':
                s = s[:-1]
                if len(s) < 6: # words like trances, chances, fences,
                               # gates, sizes, etc.
                    return s
                elif s[-1] == 'i': # parties
                    return s
                elif s[-2:] == 'is' or s[-2:] == 'iz' or s[-2:] == 'at' or\
                     s[-2:] == 'ag':
                    s = s[:-2] # characterizes, differentiates, breakages
                    return s
                elif s[-3:] == 'ifi' or s[-3:] == 'enc' or s[-3:] == 'anc' or\
                     s[-3:] == 'eri':
                    s = s[:-3] # classifies, dependences, acceptances, bakeries
                    return s
                else:
                    return s
            elif s[-2:] == 'en' or s[-2:] == 'al' or s[-2:] == 'er':
                s = s[:-2] # fastens, denials, advertisers
                return s
            elif s[-3:] == 'ant' or s[-3:] == 'ent':
                s = s[:-3] # assistants, students
                return s
            elif s[-4:] == 'tion' or s[-4:] == 'sion' or s[-4:] == 'ment':
                s = s[:-4] # functions, inclusions, developments (not questions, mentions)
                return s
            else:
                return s
    elif s[-1] == 'y': # most likely adjectives and adverbs
        if len(s) < 3:
            return s
        elif s[-2] == s[-3]:
            s = s[:-2]
            return s # words like funny
        elif s[-1] == 'l' or s[-1] == 'f':
            s = s[:-1] # words ending in ly (quickly) or fy (classify)
            if s[-3:] == 'ent' or s[-3:] == 'ive' or s[-3:] == 'ous' or\
               s[-3:] == 'ful' or s[-3:] == 'ing':
                if len(s) <= 4:
                    return s # words like live(ly)
                else:
                    s = s[:-3] # words like national, dependent, attractive,
                               # continuous, beautiful, careless, drinkable, etc.
                    return s
        else:
            s = s.replace(s[len(s)-1], 'i') # party to parti
            return s
    elif s[-3:] == 'ent' or s[-3:] == 'ive' or\
         s[-3:] == 'ous' or s[-3:] == 'ful':# just adjectives
        if len(s) < 6:
            return s # words like live(ly) but doesn't apply to all words
        else:
            s = s[:-3] # words like national, dependent, attractive,
                       # continuous, beautiful, careless, drinkable, etc.
            return s
    elif s[-4:] == 'tion' or s[-4:] == 'sion' or s[-4:] == 'ment':
        if len(s) < 8:
            return s # caution, nation, comment, element (not for payment, action, elation)
        else:
            s = s[:-4]
            return s
        s = s[:-4]
    elif s[-3:] == 'ing':
        if len(s) < 6:
            return s # execeptions: icing, doing, etc
        else:
            s = s[:-3]
            if s[-1] == s[-2]:
                s = s[:-1]
                return s
            elif s[-2:] == 'is' or s[-2:] == 'iz' or s[-2:] == 'at' or\
                s[-2:] == 'ag' or s[-2:] == 'fy': # pollinating, duplicating
                s = s[:-2] # characterizing, differentiating, packaging, classifying
                return s
            else:
                return s
    elif s[-2:] == 'en':
        if s == 'given' or s == 'taken' or s == 'haven' or s == 'eaten' or\
           s == 'woven' or s == 'given' or s == 'widen' or s == 'woken' or\
           s == 'ripen' or s == 'liken' or s == 'wizen' or s == 'risen' or\
           s == 'unpen':
            s = s[:-2]
            return s
        elif len(s) < 6:
            return s
        else:
            s = s[:-2]
            return s # execeptions: spleen, pollen, lichen, etc
    elif s[-2:] == 'er':
        if len(s) < 5:
            return s # doesn't work for words like suer and dyer
        else:
            s = s[:-2]
            if s[-1] == s[-2]:
                s = s[:-1] # programmer
                return s
            if len(s) < 6:
                return s
            elif s[-4:] == 'tion' or s[-4:] == 'sion' or s[-4:] == 'ment':
                s = s[:-4] # malpractitioner, executioner, etc
                return s
            else:
                return s # doesn't work for malpractioner, revolutionizer, executioner, etc
    elif s[-1] == 'e':
        if s[-2] == 'i':
            s = s[0] + 'y'
            return s
        elif len(s) < 4:
            return s
        else:
            s = s[:-1]
            return s
    else:
        return s
    
# Part 4: Adding methods for scoring and classification

# 1

import math

def compare_dictionaries(d1, d2):
    """take two feature dictionaries d1 and d2 as inputs, and it should compute
    and return their log similarity score"""
    score = 0
    total = 0
    for i in d1:
        total += d1[i]
    for j in d2:
        if j in d1:
            score += d2[j] * math.log(d1[j]/total)
        else:
            score += d2[j] * math.log(.5/total)
    return score

def test():
    """ Sample tests. """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ Tests of our choice. """
    source1 = TextModel('theoffice')
    source1.add_file('theoffices5ep13.txt')

    source2 = TextModel('brooklyn99')
    source2.add_file('brooklyn99s5ep14.txt')

    new1 = TextModel('parks')
    new1.add_file('parksandrecs5ep14.txt')
    new1.classify(source1, source2)
