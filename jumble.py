#NOTE: Global variables make sense for the requirements of this script, but in practice should be stored in a class instance to protect from mutation by unrelated methods. 

#Word list data structure: for large word list I will use a trie structure, which has log(n) lookup for strings

#Python marisa-trie implementation https://github.com/kmike/marisa-trie
import marisa_trie

words = marisa_trie.Trie([line.rstrip() for line in open("textFiles/english.0", "r")]) #create marisa_trie and store it in words

results = []

#Recursive jumble function permutes all values of an input string, and stores the permutations that match trie values in the results array
def jumble(input_str):
  if len(input_str) <= 1: #recursive base case
    return [input_str]
  res = []
  for letter in input_str:
    permutations = jumble(input_str.replace(letter, "", 1)) #call jumble recursively, assign result to 'permutations'
    for permutation in permutations:
      result = letter + permutation #reconstruct result of recursively permuted values
      if unicode(result) in words and (result) not in results: #add result to results list if result exists in the trie
        results.append(result)
      res.append(result) #construct a full list of permutations to return for recursive completeness
  return res  


input_str = raw_input('Enter a string:') #assign user input to input_str variable

jumble(input_str.lower()) #pass a lowercase input_str value to the jumble function

print results #print the results array

