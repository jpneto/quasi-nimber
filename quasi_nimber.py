# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:03:58 2021
@author: João Pedro Neto (code), Carlos Santos & Alexandre Silva (algorithm)
"""
from math import log2,ceil
from collections import Counter

def force(player1, player2):
  """ 
  which nimbers can player2 force on player1? 
  complexity O(|player1|*|player2|)
  """
  if len(player1) > len(player2):
    return set()
  
  dic = Counter()
  for x in player1:
    for y in player2:
      dic[x^y] += 1
  vals = { k for k,v in dic.items() if v==len(player1) }
  return vals # {min(vals)} if vals else set()


def next_pow2(m):
  """ next power of 2 strictly larger than max(m) """
  maxs = lambda s : max(s) if s else 0
  pow2 = lambda x : int(pow(2,ceil(log2(x+0.1)))) # next power of 2
  
  max_n = 0
  for row in range(len(m)):
    for col in range(len(m)):
      max_n = max(max_n, maxs(m[row][col][0]), maxs(m[row][col][1]))
  result = pow2(max_n)
  return result if result>0 else 1


def copy_del(xs, i):
  """ make a copy of xs but remove xs[i] """
  ys = xs[:]
  del ys[i]
  return ys


def unsafe(xs):
  """ return the indexes were xs[i] is false """
  return { i for i,x in enumerate(xs) if not x }
 
   
def analyse(m, Ls, Rs):
  """ given table m with unsafe moves, eval position """
  n = len(Ls)
  pow2 = next_pow2(m) 
  # starting from nimber *pow2 the first player wins,
  # we only need to check unsafe moves for smaller nimber values  
  left_opts, right_opts = [False]*pow2, [False]*pow2
  
  for y in range(pow2):   # for each nimber upto pow2-1
  
    if not left_opts[y]: # if *y not found already safe, check if it is
      # check left unsafe moves
      y_safe = False
      for i in range(n):    # for each row 
        if y_safe:
          break
        for k in Ls[i]:       # for each left move
          k_wins = True
          for j in range(n):    # for each column 
            if not k_wins:
              break
            for k1 in Rs[j]:      # for each right move
              # print('---',Ls[i],k,Rs[j],k1)
              if k^k1^y in m[i][j][0]:  # k is a losing move
                k_wins = False
                # print("y=",y,k,k1, m[i][j][0])
                break
          # if k wins all columns, we found a winning move
          y_safe = y_safe or k_wins # only unsafe if all k's are losing moves
      left_opts[y] = y_safe
    
    if not right_opts[y]: # if not found already safe, check if it is
      # check right unsafe moves
      y_safe = False
      for j in range(n):    # for each column
        if y_safe:
          break
        for k in Rs[j]:       # for each right move
          k_wins = True
          for i in range(n):    # for each row
            if not k_wins:
              break
            for k1 in Ls[i]:      # for each left move
              if k^k1^y in m[i][j][1]:  # k is a losing move
                k_wins = False
                break
          y_safe = y_safe or k_wins
      right_opts[y] = y_safe    
    
    # now check if a shortcut exists
    if not left_opts[y] and right_opts[y]:
      # y is unsafe for Left but safe for Right
      # Right wins the remaining y values: if he's playing, just move to y
      for a in range(y+1,pow2):
        right_opts[a] = True
    elif left_opts[y] and not right_opts[y]:
      # symmetric position
      for a in range(y+1,pow2):
        left_opts[a] = True
    elif not left_opts[y] and not right_opts[y]:
      # y is unsafe for both players, so all the next options are safe
      for a in range(y+1,pow2):
        left_opts[a] = right_opts[a] = True
  
  # return the pair of unsafe values, ie, (LU(L,R), LU(R,L))
  return (unsafe(left_opts), unsafe(right_opts))
  

def solve(Ls, Rs):
  assert len(Rs)==len(Ls)
  n = len(Ls)
  
  if n==1:              
    vals1 = force(Ls[0],Rs[0]) # LU(L,R)
    vals2 = force(Rs[0],Ls[0]) # LU(R,L)
    vals = vals1 & vals2
    if vals:
      return {min(vals)}, {min(vals)}
    return vals1, vals2
  
  # if n>1, iterate all valid combinations
  m = [ [0]*n for _ in range(n) ]   # table with unsafe moves
  for i in range(n):
    new_Ls = copy_del(Ls,i)
    for j in range(n):
      new_Rs = copy_del(Rs,j)
      m[i][j] = solve(new_Ls, new_Rs)

  return analyse(m, Ls, Rs)