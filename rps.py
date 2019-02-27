# import random module 
import random 
comp_point=0
user_point=0
while True: 

    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    choice = int(input("User turn: ")) 
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 

    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'

    print("user choice is: " + choice_name) 
    print("\nNow its computer turn.......") 

    comp_choice = random.randint(1, 3) 
      

    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 

    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
    # condition for winning 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
    # Printing either user or computer wins 
    if result == choice_name: 
        print("<== User wins ==>") 
        user_point=user_point+1
    else: 
        print("<== Computer wins ==>") 
        comp_point=comp_point+1
    print("User Point = ",user_point)
    print("Computer Point = ",comp_point)
    if (user_point==3):
    	print("user win the game. Thank you")
    	exit()
    if (comp_point==3):
    	print("Computer win the game. Thank you")
    	exit()


	
	
	
		    	  


		
