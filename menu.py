def menu(options):
    while True:
        user_choice = input(f'Choose from {options}: ').strip()
    
        if user_choice in options:
            return user_choice
    
        print(f'{user_choice} is invalid; choose from {options}.')
        