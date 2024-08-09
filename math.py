import re

line = 'python is a programming language'

x = re.match('python',line)

print(x)

y = re.search('is',line)

print(y)

if y:
    print('match found')
else:
    print('no match found')


x = re.sub('programming','high level programming language',line)

print(x)


line = 'python is a programming language python is a high level language'

x = re.sub('python','java',line,1)
print(x)

#\d numeric
#\D exclude
#\S exclude whitespace
#\s exc space


