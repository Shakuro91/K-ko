username = input("Enter username:")
print("Username is: " + username)  
def rysujplansze(pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9):
    thislist = [(pole1, pole2, pole3), (pole4, pole5, pole6), (pole7, pole8, pole9)]
    for x in thislist:
        print(x)

import os
os.system('cls')
plansza = range (0,9)
plansza2 = ["o","o","o","o","o","o","o","o","o"]
for x in plansza:

    gdziewstawiepionka=input() 
    if (x % 2) == 0:
     plansza2[int(gdziewstawiepionka)] = "x" 
    else:
     plansza2[int(gdziewstawiepionka)] = "O" 
    os.system('cls')
    rysujplansze(plansza2[0], plansza2[1], plansza2[2], plansza2[3], plansza2[4],plansza2[5], plansza2[6], plansza2[7],plansza2[8]) 


 