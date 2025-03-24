def num_check(question, num_type, exit_code=None):
    """Checks if user(s) enter an integer / float that is more than zero
       (or optional exit code)"""
    
    if num_type == 'integer':
        error = "Oops - please enter an integer that is more than zero"
        change_to = int
    else:
        error = "Oops - please enter a number that is more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        #checks if the user enters the exit code
        if response == exit_code:
            return response
        
        try:

            # changes the response to an integer, checking if it's more than zero

            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

#main routine goes here

#loop for testing purposes
while True:
    print()

    my_float = num_check(question = 'please enter a number that is more than 0: ', num_type = 'float')
    print(f"Thanks, you chose {my_float}")
    print()
    my_int = num_check(question = "please enter an integer that is more than 0: ", num_type = 'integer', exit_code = "")

    if my_int == "":
        print("You have chosen infinite mode")
    else:
        print(f"Thanks. You chose {my_int}")


