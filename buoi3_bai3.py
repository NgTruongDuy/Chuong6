# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:48:13 2024

@author: NguyenTruongDuy
"""

a = int(input("Nhap so nguyen co 2 chu so: "))
if a>=10 and a<=99:
    pd = a%10
    pn = a//10
    s = pd+pn
    print("Tong cac chu so cua a: ",s)
else:
    print("Khong hop le")
    
