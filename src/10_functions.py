# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

def is_even(number):
    # int(number)
    while True:
        try:
            if int(number) == 0:
                return'Is zero even or odd???'
                
            else:
                if not int(number) % 2:
                    return"Even!"
                    
                else:
                    return'Odd'
                    
        except ValueError:
            return'Please try again, but this time enter a number'
            
        except TypeError:
            return'Please try again, but this time enter a number'
            



# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if __name__ == '__main__':
    num = input("Enter a number: ")
    print(is_even(num))

