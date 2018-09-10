def manual():
    new_guess = 50
    guess_limit_up = 100  
    guess_limit_down = 0
    guess_count = 0
    user_inp = "not ok"
    print("Manual: ")
    try:
        while user_inp != "ok" : 
            user_inp = input("My guess is " + str(int(new_guess)) + " . Is your number up, down, or ok? ")
            guess_count +=1
            if user_inp =="up":
                guess_limit_down = new_guess
                new_guess = ((guess_limit_up + new_guess)/2)        
            elif user_inp == "down":
                guess_limit_up = new_guess 
                new_guess = ((new_guess-guess_limit_down ) /2)        
        print("I got it in " + str(guess_count) + " guesses!")
    
manual()




    



    

    
    
