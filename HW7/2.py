import string

class Count:
    def __init__(self):
        self.word_counts = {}
        print("Word Counter Initialized")
    
    def get_num_words(self):
        return len(self.word_counts)
    
    def increment_count(self, word):
        cleaned_word = word.lower().strip(string.punctuation)
        if not cleaned_word:
            return
        if cleaned_word in self.word_counts:
            self.word_counts[cleaned_word] += 1
        else:
            self.word_counts[cleaned_word] = 1
    
    def lookup_count(self, word):
        return self.word_counts.get(word, 0)
    
    def get_top_words(self, num):
        return

def main():
    counter = Count()
    
    # Ensure Parts 3 and 4 test code is commented
    filename = input("Enter book file: ")
    with open(filename) as infile:  # Use 'with' for better file handling
        for line in infile:
            words = line.split()
            for word in words:
                counter.increment_count(word)
    
    # Test code for Parts 5 and 6
    print("alice:", counter.lookup_count("alice"))
    print("rabbit:", counter.lookup_count("rabbit"))
    print("and:", counter.lookup_count("and"))
    print("she:", counter.lookup_count("she"))
    print("Unique words:", counter.get_num_words())

main()
