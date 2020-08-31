dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print dict['a']     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict: print dict['z']     ## Avoid KeyError
print dict.get('z')  ## None (instead of KeyError)

dict1 = {}
dict1[1] = 'alpha'
dict1[2] = 'gamma'
dict1[3] = 'omega'
print dict1

for x in dict1:
	print dict1[x]

for y in dict1:
	print dict1.get(y)

for z in dict:
	print dict.get(z)