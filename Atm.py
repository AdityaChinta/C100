class Atm:
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
    def check_balance(self):
        print('Your balance is 100000.')
    def withdrawl(self,amount):
        new_amount=100000-amount
        print('You have withdrew'+str(amount)+'.The remaining balance is '+str(new_amount))

def main():
    cardnumber=input('Insert your Card Number:')
    pin_number=input('Enter your Pin:')
    newuser=Atm(cardnumber,pin_number)
    print('Choose your activity')
    print('1.Balance Enquiry  2.Withdrawl')
    activity=int(input('Enter Activity Number:'))

    if(activity==1):
        newuser.check_balance()
    elif(activity==2):
        amount=int(input('Enter the Amount:'))
        newuser.withdrawl(amount)
    else:
        print('Please enter a valid number:')

if __name__=='__main__':
    main()
        