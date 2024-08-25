# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:28:14 2024

@author: NguyenTruongDuy
"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

c = ((a**(1/2)-b**(1/2)) / (a**(1/4)-b**(1/4))) - ((a**(1/2)+(a*b)**(1/4)) / ((a**(1/4))+b**(1/4)))
print("Ket qua la: ",c)
