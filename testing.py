'''id=''
name=''
age=''
position=''
n=''
def input():
    n=int(input("Enter Number Of person :"))
    for i in range(n) :
        id=input("Enter ID :")
        name=input("Enter Name :")
        age=input("Enter Age :")
        position=input("Enter Ur Position :")
       
def output():
    for i in range(n):
        print("ID :"+id)
        print("Name :"+name)
        print("Age :"+age)
        print("Position :"+position)
    
        
input()
output()'''

import random

x = random.randint(1, 20)
try:
    num = int(input("Input Number from 1 to 20: "))
    print("Random number:", x)
    if num == x:
        print("You Win!")
    else:
        print("You Lose! The correct number was", x)
except :
    print("Ohh, You need to input an integer!")
