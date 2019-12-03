# PRINT 0 1 2 3 4 
# for n in range(5):
#   print(n)

# PRINT 3 4 5 6 7 8 9
# for n in range(3,10):
#   print(n)

# PRINT 0 4 8 12 16
# for n in range(0,20,4):
#   print(n)


burgers=['beef', 'chicken', 'veg', 'supreme', 'double']

# PRINT 0beef 1chicken 2veg 3supreme 4double
# for n in range(len(burgers)):
#   print(n,burgers[n])

# PRINT array backwards
for n in range(len(burgers)-1,-1,-1):
  print(n,burgers[n])