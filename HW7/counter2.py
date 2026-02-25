#count2.py
#Jiawei Zhu
#
#Writing a word counting class and making a wordle
# import wordle
import string

#
# The Count class
#
# The class keyword below begins the definition of a new Python data type Count.
# Count keeps word counts. All the methods that we can use with Count objects
# and the variables (attributes) built inside Count objects are defined in the
# this class definition.

class Count:
        #The Count class in here that helps words in a dictionary
        def __init__(self):
                #Initialize word_counts to an empty dictionary
                self.word_counts = {}
                #Print the message when the word counter initaialized
                print("Word Counter Initialized")
                
        def get_num_words(self):
                #The get_num_words method returns the number of words
                #(keys) in the word_counts dictionary.
                #This counts each word only once.
                #Return to check the totally unique word in the dictionary
                return len(self.word_counts)


        def increment_count(self,word):
                return


        def lookup_count(self,word):
                return


        def get_top_words(self,num):
                return
        
# The main program 
def main():
                                
        ## Make a new Count object 
        ## the counter object will keep track of
        ## the counts for all the words in the book
        counter = Count()

  

        print("Unique words:", counter.get_num_words())
        


# Call the main program
main()
        
