# Functions Go Here
def string_check(question, valid_ans_list):
    """Checks that users enter the full word
       or the first letter of a word from a list of valid responses"""
    
    while True:

        response = input(question).lower()

         # checks if the response is exactly the same as the word
        if response in valid_ans_list:
            return item

        

        for item in valid_ans_list:
            # checks if the response is exactly the same as the word
            if response == item:
                return item

            # checks if the response is exactly the first letter of the word
            elif response == item[0]:
                return item
            
            print(f'Please choose an option from {valid_ans_list}')
    
# Main Routine Goes Here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check('Do You Like Coffee? ', valid_ans_list = ['yes', 'no'])
print(f'You Chose {like_coffee}')
Difficulty = string_check('Set Your Difficulty ', levels)
print(f'You Chose {Difficulty}')