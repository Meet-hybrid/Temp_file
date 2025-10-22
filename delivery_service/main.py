from delivery import get_riders_wage

main= """
   	 ==== BACK TO SENDER LOGISTICS MENU ====
    |_______________________________________________|  
    |Collection Rate   |Amount Per Percel|Base Pay  |
    |__________________|_________________|__________|
    | 1 |Less than 50% |           160   | 5000     |
    |__________________|_________________|__________|
    | 2 |50% - 59%     |           200   | 5000     |
    |__________________|_________________|__________|
    | 3 |60% - 69%     |           250   | 5000     |
    |__________________|_________________|__________|
    | 4 |70% and above |           500   | 5000     |
    |__________________|_________________|__________|
    | 5 | Exit         |                 |          |
   ==================================================
"""
print(main)
while True:
	choice = int(input("\nSelect case (1-5): "))

	match choice:
		case 1:
			percent = float(input("Enter percentage (<50): "))
			print(f"Rider's wage: {get_riders_wage(percent)}")			
		case 2:					
			percent = float(input("Enter percentage (50–59): "))
			print(f"Rider's wage: {get_riders_wage(percent)}")
		case 3:
			percent = float(input("Enter percentage (60–69): "))
			print(f"Rider's wage: {get_riders_wage(percent)}")
		case 4:		
			percent = float(input("Enter percentage (70–100): "))
			print(f"Rider's wage: {get_riders_wage(percent)}")
		
		case 5:
			print("Exiting program... Goodbye!")
			break
		case _:
			print("Invalid choice, try again.")
			
        
        
            

