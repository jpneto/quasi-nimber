# -*- coding: utf-8 -*-

from quasi_nimber import solve

Ls = [{0,1,2,3,6}, {5,6}]  
Rs = [{1,2},       {0,1,2,3,4,6,7}]
print(solve(Ls, Rs))

Ls = [{1,3}, {3,5,6}]
Rs = [{1,3}, {3}]
print(solve(Ls, Rs))

Ls = [{2}, {1}, {4}]
Rs = [{1}, {0}, {2,6}]
print(solve(Ls, Rs))

Ls = [{2,4,6}, {1,2}, {1,4}, {6,7}, {1,4,7}]
Rs = [{1,2,3}, {1,3}, {2,6}, {1,2}, {1,2,3,4,5}]
print(solve(Ls, Rs))

Ls = [{5,6}]
Rs = [{1,2}]
print(solve(Ls, Rs))

Ls = [{5,7}]
Rs = [{1,2}]
print(solve(Ls, Rs))

Ls = [{5,6}]
Rs = [{0,1,2,3,4,6,7}]
print(solve(Ls, Rs))

Ls = [{0,1,2,7}, {0,3,5}, {0}]
Rs = [{2}, {1,6,8}, {3,7}]
print(solve(Ls, Rs))