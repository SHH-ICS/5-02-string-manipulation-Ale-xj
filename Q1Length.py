# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
word = ''
while word != 'quit': 
  word = input("Sumbit a word ('quit' to exit): ")
  if word != 'quit':
    print(f"the word is {len(word)} charecters long.")
print("program ended")
