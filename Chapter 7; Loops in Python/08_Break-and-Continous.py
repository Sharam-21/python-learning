

for i in range (100):
  if(i==10):
    break     # Exist from the loop rightnow.

  print(i) # this will print 0,1,2 and 3, 4, 5, 6, 7, 8, 9


for i in range(10):
  if(i==7):
    continue        # Skip this only iteration and continue with the next iteration.

  print(i)     
'''Output is like this, Skip only 7 :
0
1
2
3
4
5
6
8
9'''

