my_name='ryu'

def print_name():
  global my_name #Overrrides global variable for both
  my_name='yoshi'
  print('the name inside the function is', my_name)

print_name()
print('outside the function the name is', my_name)