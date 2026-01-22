'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)     # {'20', 20} . Bcz 20 or 20.0 is same and in set same value is written once.
print(len(s))    #  2


