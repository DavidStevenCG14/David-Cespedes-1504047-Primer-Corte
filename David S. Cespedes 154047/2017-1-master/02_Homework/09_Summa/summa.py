#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even.py
# Description: This module separates a list of integers into two lists (odd, even)
# Author: Diego Fernando Marin
n = int(input("ingrese el numero n:"))
m = int(input("ingrese el numero m:"))
suma = 0 
p=0
if n > m:
	print("n debe ser mayor que m")
else: 
	for x in range(n,m+1):
		suma+= x**2 + 2*6
	print (suma)