import re 

# print(re.split(r'(s*)', 'here are some words'))

print(re.split(r'[a-f][a-f]', ';farcdfromfeekla;FLFPALFAf',
    re.I|re.M))

a = 'This is my string'
print(a[1:5])
print(a[2:])
print(a[2:5])
print(a[:7])
print(a[0:-1])
print(a[:])
print(a[0:9:2])
print(a[0:9:3])
print(a[::3])
print(a[::-1])
print(a[::-2])

print(a[slice(None,None,2)])
print(a[slice(1,9)])