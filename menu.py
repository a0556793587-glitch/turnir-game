menu = """1. Add team
2. Show all teams
3. Add match result
4. Show standings
5. Show leading team
6. Show best attacking team
7. Show team success rate
8. Show teams without wins
9. Show tournament summary
10. Check championship potential
0. Exit
Choose an option:"""
def print_menu():
    print(menu)   

def get_input():
    choose_number = None
    while True:
        try:
            choose_number = int(input("enter your anser!"))
            if choose_number >= 0 and choose_number < 11:
                return choose_number
            elif choose_number > 10 or choose_number < 0:
                print("Incorrect option Try again")
        except ValueError:
            print("You must choose only from the possible options, so you will choose between 0 and 10.")
    
