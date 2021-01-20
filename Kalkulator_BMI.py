# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:52:26 2021

@author: Mateusz C
"""


### BMI Calc


print("BMI Calculator")
print(100* "*")

name  = input("Podaj imię: ")
weight = float(input("Podaj wagę: "))
print("Wpisz wzrost po kropce(np: 180cm to 1.8m)")
heigh = float(input("Podaj wzrost: "))

bmi = weight/(heigh**2)

if ( bmi < 16):
   print(f"{name} wystąpiła u Ciebie poważna niedowaga.Wskaźnik BMI wynosi {bmi}")

elif ( bmi >= 6 and bmi < 18.5):
   print(f"{name} wystąpiła u Ciebie niedowaga.Wskaźnik BMI wynosi {bmi}")

elif ( bmi >= 18.5 and bmi < 25):
   print(f"{name} Twój wskaźnik BMI jest prawidłowy, wynosi{bmi}")

elif ( bmi >= 25 and bmi < 30):
   print(f'{name} wystąpiła u Ciebie nadwaga.Wskaźnik BMI wynosi{bmi}')

elif ( bmi >=30):
   print(f"{name} wystąpiła u Ciebie poważna niedowaga.Wskaźnik BMI wynosi {bmi}")        
    
