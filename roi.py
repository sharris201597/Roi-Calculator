


class Property:
    def __init__(self,address,buildingType):
        

        self.address = address
        self.buildingType = buildingType
        self.income = {}
        self.expenses = {}
        self.investments = {}


    def trackExpences(self): 
        print("\nPlease enter only digits/numbers for the following questions!")
     # This protion of method tracks MANDORTORY things to calculate expenses

        # Tracks Property Tax
        propertyTax = input("\nWhat are the properrty taxes estamated to be for this property each month?")
        if propertyTax.isdigit() != True:
            print("Please enter a digit/number...")
            self.trackExpences()
        else:
            self.expenses['Property Tax'] = int(propertyTax)

        # Tracks Insurance
        while True:
            insurance = input("\nWhat is your insurance payment on this property? Each Month? ")
            if insurance.isdigit() == False:
                print("Please enter a digit/number...")
            else:
                self.expenses['Insurance'] = int(insurance)
                break
                
        # Tracks Utilities
        while True:
            utilities = input('\nWhat is the total sum of utilities each month? ')
            if utilities.isdigit() == False:
                print("Please enter a digit/number...")
            else:
                self.expenses['Utilities'] = int(utilities)
                break

        # Tracks Morgage
        while True:
            morgage = input('\nWhat is your morgage payment each month? ')
            if morgage.isdigit() == False:
                print("Please enter a digit/number...")
            else:
                self.expenses["Morgage"] = int(morgage)
                break 
        
        # Tracks optional/additional expences
        flag = True 
        while flag: 
            answer = input("""
                      Any other expenses you would like to add?

                       Enter [y] for yes
                                                
                       Enter [n] for no
                      """).lower().strip()

            if answer in ('n','no'):
                flag = False
            elif answer in ('y','yes'):
                print('\nWhat is the type of expense you would you like to add? ')
                extraExpense = input(("...for ex: Hoa Fees, repairs , etc....  ").lower().strip())
                while True: 
                    extraExpenseCost = input(f"\nHow much does {extraExpense} cost a month?")
                    if extraExpenseCost.isdigit() == False:
                        print("Please enter a digit/number...")
                    else: 
                        extraExpenseCost = int(extraExpenseCost)
                        self.expenses[extraExpense] = extraExpenseCost
                        break

            total = sum(self.expenses.values())         
            print(f"Your Total expenses from this property at {self.address} is {total} ")
            
    

    def trackIncome(self):

        # Tracks Rental Income
        rentIncome = input("How much rental income is expected a month from this property?  ")
        if rentIncome.isdigit() == False:
            print("Please enter a digit/number")
            self.trackIncome()
        else:
            
            self.income["Rental Income"] = int(rentIncome)

        # Tracks additional/optional income of the property
        flag = True
        while flag: 
            answer = input(("""
                                Any other incomes for this property we should know about?

                                            Enter [y] for yes
                                            
                                            Enter [n] for no 

                                                    """).lower().strip())
            if answer in ('no', 'n'):
                flag = False
                
            elif answer in ('y','yes'):
                print('\nWhat type of extra monthly income would you like to include in the roi calculation? ')
                extraIncomeType = input("... for ex: Laundry, Vending Machines, ATMs, etc... ").lower().strip()

                while True: 
                    extraIncome = input(f"\nHow much income does {extraIncomeType} bring in a month for this property?")
                    if extraIncome.isdigit() == False:
                        return print("Please enter a digit/number...")
                    else:
                       
                        self.income[extraIncomeType] = int(extraIncome)
                        self.totalIncome =+ int(extraIncome)
                        break
                        
            else:
                print("\nInvalid Input")
                print("Please enter either [Y] for 'yes' of [N] for 'no' ")
        total = sum(self.income.values())
        return print(f"Your Total income from this property at {self.address} is {total}")


    def cashFlow(self):
        totalIncome = sum(self.income.values())
        totalExpenses = sum(self.expenses.values())
        cashFlow = totalIncome - totalExpenses
        
        # print(f"\nYour monthly cash flow at this property at {self.address} is {cashFlow} a month")
        return cashFlow
    

    def trackInvestments(self):
        # Tracks the down payment for property

        while True: 
            downPayment = input(f"What was your down Payment for {self.address}?")
            if downPayment.isdigit() == False:
                print("Please enter a digit/number")
            else: 
                self.investments['Down Payment'] = int(downPayment)
                break
        # Tracks other/additional investments like closing cost, rehab, etc...

        flag = True
        while flag:
            answer = input(f"""
                                Any additional investments for this property at {self.address}?

                                            Enter [y] for yes
                                            
                                            Enter [n] for no 
                                                    """).lower().strip() 
            if answer in ('n', 'no'):
                flag = False
            elif answer in ('y', 'yes'):
                print(f'\nWhat is the type of investment you would you like to add? For {self.address}')
                extraInvestmentType = input("...for ex: Rehab, Closing costs, etc....? ").lower().strip()
                while True:
                    extraInvestmentCost = input(f"\nHow much did {extraInvestmentType} cost for this property at {self.address}?")
                    if extraInvestmentCost.isdigit() == False:
                        return print("Please enter a digit/number...")
                    else:
                        self.investments[extraInvestmentType] = int(extraInvestmentCost)
                        break 
            else:
                print("\nInvalid Input")
                print("Please enter either [Y] for 'yes' of [N] for 'no' ")

        total = sum(self.investments.values())
        print(f"Your total investment for this property at {self.address} is {total}")

    # Determines yearly roi
    def roi(self):
        monthlyCashFlow = self.cashFlow()
        totalInvestment = sum(self.investments.values())
        roi = (monthlyCashFlow / totalInvestment) * 2
        print(f"\nYour Yearly Roi on the propery at {self.address} is {roi}%")


    def run(self):
        self.trackExpences()
        self.trackIncome()
        self.trackInvestments()
        self.roi()




print("Welcome to Sam's ROI calculator")


flag = True

while flag:
    offButton = input("\nIf you would like to end this program enter 'q' or 'quit'. If not enter 'c' to continue! ").lower().strip()
    if offButton in ('q', 'quit'):
        flag = False
    elif offButton in ('c', 'continue'):
        userProp = Property(input("\nWhat is the address of the property you are investing in? "),
        input('What type of property is this (single family, mulit family, duplex, commercial, or other? ').lower().strip())
    else:
        print("Please enter either 'q' to quit program or 'c' to continue.")

    userProp.run()





    

                

                    


