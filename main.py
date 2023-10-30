# Ryan Mendez

global menu_choice
def encode(password):
    # shift every digit from string password up by 3 numbers
    encoded_password = ''
    for i in password:
        current_char = int(i) + 3
        encoded_password = encoded_password + str(current_char)
    return encoded_password



def main():
    # print menu
    print('Menu')
    print('-' * 8)
    print('0. Exit')
    print('1. Encode Password')
    print('2. Decode Password')

    menu_choice = int(input('\nPlease enter menu selection: '))

    while menu_choice != 0:
        if menu_choice == 1:
            original_password = input('Please enter your password to encoded: ')
            print(f'Your encoded password is: {encode(original_password)}')
        elif menu_choice == 2:
            original_password = input('Please enter your password to decoded: ')
            print(f'Your encoded password is: {decode(original_password)}')
        # print menu
        print('\nMenu')
        print('-' * 8)
        print('0. Exit')
        print('1. Encode Password')
        print('2. Decode Password')
        menu_choice = input('\nPlease enter menu selection: ')

if __name__ == "__main__": main()