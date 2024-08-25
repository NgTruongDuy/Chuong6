# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:18:38 2024

@author: NguyenTruongDuy
"""

ns = int(input("Nhap nam sinh: "))
if ns>2024:
    print("Khong hop le")
else:
    t = 2024 - ns
    print("Vay nam 2024, tuoi cua ban la: ",t)