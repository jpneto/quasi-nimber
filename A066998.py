# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:03:58 2021

@author: jpn3t
"""

# estimate number of operations given n cards for each player
# cf. https://oeis.org/A066998  a(0)=0; a(n) = n^2 * a(n-1) + 1. 

def A066998():
  n, a = 0, 0
  while True:
    yield a
    n = n+1
    a = n**2 * a + 1
    
g = A066998()
print([next(g) for _ in range(10)])
