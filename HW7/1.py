# count3.py
# Jiawei Zhu
#
# Writing a word counting class and making a wordle

# import wordle
import string

class Count:
        # The Count class helps track word occurrences in a dictionary

        def __init__(self):
                # Initialize word_counts to an empty dictionary
                self.word_counts = {}

                # Print a message when the word counter is initialized
                print("Word Counter Initialized")
                
        def get_num_words(self):
                # Return the number of unique words (keys) in word_counts
                return len(self.word_counts)

        def increment_count(self, word):
                # If word is already in dictionary, increment its count
                # Otherwise, add word with count 1
                if word in self.word_counts:
                        self.word_counts[word] += 1  # Fixed typo (was `seld`)
                else:
                        self.word_counts[word] = 1

        def lookup_count(self, word):
                # Return count of word if it exists, otherwise return 0 (without using .get())
                if word in self.word_counts:
                        return self.word_counts[word]
                else:
                        return 0

        def get_top_words(self, num):
                # Return a sorted list of the top 'num' words by count
                return sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)[:num]

# The main program 
def main():
        # Create an instance of Count
        counter = Count()

        # Test code for Part 3 and 4 (Uncommented as per instructions)
        counter.increment_count("Well,")
        counter.increment_count("oven")
        counter.increment_count("well")
        counter.increment_count("....'")
        
        print(counter.lookup_count("oven"))   # Expected output: 1
        print(counter.lookup_count("well"))   # Expected output: 1
        print(counter.lookup_count("pizza"))  # Expected output: 0
        print(counter.lookup_count(""))       # Expected output: 0

        # Print the number of unique words
        print("Unique words:", counter.get_num_words())  # Expected output: 4

# Call the main program
main()
