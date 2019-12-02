ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# PRINTS EACH INDIVIDUAL NINJA
# for ninja in ninjas:
#   print(ninja)

# PRINTS 'CRYSTAL' AND 'YOSHI'
# for ninja in ninjas[1:3]:
#   print(ninja)

# PRINTS 'RYU' 'CRYSTAL' AND 'YOSHI - BLACK BELT'
for ninja in ninjas:
  if ninja == 'yoshi':
    print(f'{ninja} - black belt')
    break
  else:
    print(ninja)