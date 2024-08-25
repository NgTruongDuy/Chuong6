# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:08:49 2024

@author: NguyenTruongDuy
"""

g = int(input("Nhap gio: "))
p = int(input("Nhap phut: "))
gy = int(input("Nhap giay: "))

dg = g*3600
dp = p*60
tt = dg+dp+gy

print("Doi don vi thoi gian thanh giay la: ",tt)