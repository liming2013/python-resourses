 # coding : utf-8
import os

def fib(n):
	a,b=0,1
	while a<n:
		a,b=b,a+b
		print a

fib(10000000)