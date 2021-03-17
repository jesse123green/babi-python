
alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]




# From Section 11.2 of:
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.




def histogram(s):
   d = dict()
   for c in s:
       if c not in d:
           d[c] = 1
       else:
           d[c] += 1
   return d



def has_duplicates(s):
   return len(histogram(s)) != len(s)


#this i found online but don’t quite understand it
def missing_letters(s):


   h = histogram(s)
   rv = ''
   # Loop over letters in alphabet, if the letter is not in the histogram then
   # append to the return string.

   for c in alphabet:
       if c not in h:
           rv = rv + c

   return rv




# Loop over test strings as required.

for s in test_miss:
   miss = missing_letters(s)
   if miss:
       print(f"{s} is missing letters {miss}.")
   else:
       print(f"{s} uses all the letters.")

