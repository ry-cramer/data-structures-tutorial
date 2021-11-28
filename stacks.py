'''
Program that determines whether a string includes balanced or unbalanced parentheses.
- Must allow any input
- Doesn't account for square or curly brackets

Written by Reb Cramer on November 27, 2021
'''
def check_parentheses(string):
    # Creates the stack
    stack = []
    # Iterates tthrough the string to check whether each character is a parenthesis
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                # Accounts for if the stack is empty (there are no opening parentheses to go with the closing parenthesis)
                return False
    # Returns True if stack is empty
    if not stack:
        return True
    # Accounts for if the stack is not empty at the end of the loop (there were no closing parentheses to go with the opening parentheses)
    return False

def main():
    run = True
    # Creates a loop that runs until program is quit
    while run:
        to_check = input('What is your string (type q to quit)?: ')
        # Checks if program is being quit
        if to_check == 'q':
            print('Thank you for using the program.')
            break
        # Checks parentheses balance
        checked = check_parentheses(to_check)
        if checked:
            print('The parentheses are balanced.')
        else:
            print('The parentheses are not balanced.')
        print('')

if __name__ == '__main__':
    main()
