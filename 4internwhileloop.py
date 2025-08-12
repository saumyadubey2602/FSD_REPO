correct_password="python123"
while True:
    password=input("enter the password")
    if password==correct_password:
        print("ACCESS GRANTED!")
        break
    else:
        print("WRONG PASSWORD,ENTER CORRECT PASSWORD")
