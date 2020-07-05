# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

def is_even(number):
    while True:
        try:
            if number == 0:
                print('Is zero even or odd???')
                break
            else:
                if not number % 2:
                    print("Even!")
                    break
                else:
                    print('Odd')
                    break
        except ValueError:
            print('Please enter a number')
            continue
        except TypeError:
            print('Please enter a number')

is_even(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

