
class Account:
    def __init__(self, accid, balance, name)
    self.accid = accid
    self.balance = balance
    self.name = name

pArray = []
index = 0

def printMenu():
    print("-------Menu--------")
    print("1. open an account")
    print("2. deposit")
    print("3. withdraw")
    print("4. inquire")
    print("5. end")

def openAnAccount():
    id = input("account id : ")
    name = input("name : ")
    money = input("money : ")
    pArray.append()
    acc1[index].balance = money
    acc1[index].name = name
    index = index + 1

def deposit():
    id = input("account id : ")
    money = input("money : ")

def inquire():
    for i in (index):
        print(acc1[i])

def end():
    exit()
    # sys.exit()
def main():
    while 1:
        printMenu()
        n = input("select a menu: ")
        if n == '1':
            deposit()
        elif n == '5':
            exit()

main()