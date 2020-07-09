"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# newer syntax, makes closing unneccesary
with open("src/foo.txt", mode="r") as file:
    print(file.read())

alt_file = open("src/foo.txt")
print('\n', alt_file.read())
alt_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# bar_file1 = open("src/bar.txt", 'w')
# bar_file1.write('This is the first line.\nThis is the second line.\nGuess which line this is?')
# bar_file1.close()


# bar_file1_read = open("src/bar.txt")
# print('\n', bar_file1_read.read())
# bar_file1_read.close()

# with open("src/bar.txt", mode="w") as bar_file:
#     bar_file.write('This is the first line.\nThis is the second line.\nGuess which line this is?')

# bar_file_read = open("src/bar.txt")
# print(bar_file_read.read())