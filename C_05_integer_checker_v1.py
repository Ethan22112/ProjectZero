def num_check(question):
    """Checks if user(s) enter an integer / float that is more than zero
       (or optional exit code)"""
    
    error = "Oops, please enter an integer that is more than zero"
    
    while True:
        response = input(question).lower

        #checks for the exit code
        if response == "xxx":
            return response
        
        try:
            #changes the response into an integer, checking whether its value is more than zero
            response = int(response)

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

    #asks user for an integer
    my_num = num_check('Choose a number that is more than zero')
    print(f'You chose {my_num}')


