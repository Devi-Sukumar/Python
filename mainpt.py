#Python program to call a function that calculates the Pythagorean triples 
#which is lesser than the user provided value

import Pytriples #import the file that has user defined function

n=int(input("Enter a number to calculate Pythagorean triples:"))

Pytriples.pytriples(n)
