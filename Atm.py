class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 99000 rupees")

    def withdraw(self,amount):
        if amount > 99000:
            print("You have only 99000 rupees in your account, you cannot withdraw "+str(amount)+" rupee(s)")
            
        else:
            new_amount = 99000 - amount
            print("Your Transaction Is Under Process, Please Wait....")
            print("You have withdrawn "+str(amount) +" rupee(s). Your remaining balance is "+ str(new_amount)+" rupee(s)")
            print("Hope To See You Again")
            print("ThankYou")

            
        

def main():
    Card_number = input("Kindly Insert Your Card Number:- ")
    pin_number  = input("Kindly Enter Your Pin Number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose Your Activity ")
    print("1.Balance Enquiry   2.Withdraw Money")
    activity = int(input("Please Enter The Activity Number To Proceed :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Please Enter The Amount:- "))
        new_user.withdraw(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()