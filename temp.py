# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

"""
s = ""
d = 0;
s = str(input("Nhap diem chu: "))
if s != "A+" or s != "A" or s != "A-" or s != "B+" or s != "B" or s != "B-" or s != "C+" or s != "C" or s != "C-" or s!= "D" or s!= "F": 
    while s != "A+" and s != "A" and s != "A-" and s != "B+" and s != "B" and s != "B-" and s != "C+" and s != "C" and s != "C-" and s!= "D" and s!= "F": 
        print("Yeu cau nhap lai")
        s = str(input("Nhap diem chu: "))    
    if(s == "A+" or s == "A" ):
        d = 4.0        
    elif (s == "A-"):
        d = 3.7
    elif (s == "B+"):
        d = 3.3
    elif (s == "B"):
        d = 3.0
    elif (s == "C+"):
        d = 2.7
    elif (s == "C"):
        d = 2.0
    elif (s == "C-"):
        d = 1.7    
    elif (s == "D+"):
        d = 1.3
    elif (s == "D"):
        d = 1.0
    else:
        d=0
    print("Diem cua ban la:",d)
"""

"""


try:    
    r = float(input("Nhap rate cua ban: "))             
    while r < 6:  
        if(r == 4 or r == 0):
            break        
        print("Yeu cau nhap lai")
        r = float(input("Nhap rate cua ban: "))             
    if(r == 0):
        print("unacceptable")
    elif(r == 4):
        print("acceptable")
    else:
        print("meritorious")
except:
    print("Vui long nhap so")
"""

"""
try:        
    n = int(input("Nhap nam: "))
    while(n < 0):
        print("NHap lai")
        n = int(input("Nhap nam: "))
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print("Nam",n,"la nam nhuan!!!")
    else:
        print("Nam",n,"khong phai nam nhuan!!!")
except:
    print("Voi long chi nhap so")            
        
"""

"""
try:    
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    c = int(input("Nhap so c: "))
    if(a == 0):        
        if(b == 0 ):     
            if(c==0):
                print("Phuong trinh vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            x = -c / (2 * b)
            print("Phuong trinh co 1 nghiem duy nhat x=",format(x,".3")) 
           
    else:            
        delta = b*b - 4 * a * c
        if(delta > 0):
            x1 = (-b + math.sqrt(delta))/ (2 * a)
            x2 = (-b - math.sqrt(delta))/ (2 * a)
            print("Phuong trinh co 2 nghiem duy nhat la:")
            print("x1=",format(x1,".3"))
            print("x1=",format(x2,".3"))        
        elif(delta == 0):
            x = -b / (2 * a)
            print("Phuong trinh co 1 nghiem duy nhat x=",format(x,".3"))        
        else:
            print("Phuong trinh vo nghiem")
except:
    print("Chi nhap so")
"""


"""
try:
    a = int(input("Nhap so a: "))
    b = float(input("Nhap so b: "))
    c = float(input("Nhap so c: "))  
    ta = a
    tb = b
    tc = c  
    if(a < 0):
        a = -a
    if(b <0):
        b = -b
    if(c<0):
        c = -c
    if(a < 10):
        print(ta)
    if(b < 10):
        print(tb) 
    if(c < 10):
        print(tc)
except:
    print("Chi nhap so")
"""


"""
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
d = int(input("Nhap so d: "))
e = int(input("Nhap so e: "))
print("Max =",max(a,b,c,d,e))
print("Min =",min(a,b,c,d,e))
"""

"""
year = int(input("nhap nam: "))
day = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7
if(day == 0):
    print("Chu nhat")
elif(day == 1):
    print("Thu 2")
elif(day == 2):
    print("Thu 3")
elif(day == 4):
    print("Thu 5")
elif(day == 5):
    print("Thu 6")
elif(day == 6):
    print("Thu 7")
"""

"""
thang =int(input("nhap thang: "))
if(thang >= 1 and thang <= 12):
    print("Hop le")
else:
    print("Khong hop le")
"""

"""
x = int(input("Nhap so x: "))
if(x > 0):
    kq = x*x + 3 * x + 5
else:
    kq = -1 * (x*x) - 3 * x -5
print(kq)
"""



"""

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
d = int(input("Nhap so d: "))
e = int(input("Nhap so e: "))
sd =0
sa =0
if(a>=0):
    sd += 1
if(b>=0):
    sd += 1
if(c>=0):
    sd += 1
if(d>=0):
    sd += 1
if(e>=0):
    sd += 1

if(a<0):
    sa += 1
if(b<0):
    sa += 1
if(c<0):
    sa += 1
if(d<0):
    sa += 1
if(e<0):
    sa += 1
print("sl so duong la:",sd)
print("sl so am la:",sa)
"""

"""
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
if(a%2==0):
    if(b%2==0):
        print("a va b la so chan")
    else:
        print("co 1 so la so chan")
elif(b%2==0):
        print("co 1 so la so chan")
else:
    print("a va b la so le")
"""

"""
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
if(a%b==0):
    print(a,"la boi so cua",b)
else:
    print(a,"khong phai boi so cua",b)
"""

"""
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
ktra = False
if(a > 0):
    min = a
    ktra = True
elif(b > 0):
    min = b
    ktra = True
elif(c > 0):
    min = c
    ktra = True
if(ktra):
    if(b < min and b > 0):
        min = b
    elif(min > c and c > 0):
        min = c
    print(min)
else:
    print("Khong co so duong")
"""


"""
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
ktra = False
if(a%2==0 ):
    maxc = a
    ktra = True
elif(b%2==0  ):
    maxc = b
    ktra = True
elif(c%2==0 ):
    maxc = c
    ktra = True

if(ktra):
     if(maxc < b and b%2==0):
         maxc = b
     elif(maxc < c and c%2==0):
         maxc = c
     print(maxc)
else:
    print("Khong co so chan")
"""




    