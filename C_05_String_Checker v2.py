# Functions Go Here
def string_check(question, valid_ans_list = ('yes', 'no'), num_Letters = 1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""
    
    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            # checks if the response is either exactly the same as the word
            if response == item:
                return(item)

            # checks if the response is exactly the first letter of the word
            elif response == item[:num_Letters]:
                return(item)
            
            print(f'Please choose an option from {valid_ans_list}')
    
# Main Routine Goes Here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']


like_coffee = string_check('Do You Like Coffee? ', yes_no_list, num_Letters = 1)
print(f'You Chose {like_coffee}')
pay_method = string_check('Payment Method: ', payment_list, num_Letters = 2)
print(f'You Chose {pay_method}')