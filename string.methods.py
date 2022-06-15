p="SHAinaz SHeik"
print(p.swapcase()) 

# a=4  ; b=66
# print(a)
# del a,b
# print(a,b)

# """format"""

# print("im {d}.my number is {ed}.".format(d='shainaz',ed='**********'))

# '''expandtabs  , by default=8'''
# a='s\th\tn'
# print(a.expandtabs(0))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs())
# print(a.expandtabs(-1))

# """ join """
# v='hello','python','core'
# n='python'
# print('-'.join(v))
# print('*'.join(n))
# print('*'.join("python"))

""" maketrans and translate"""
# r="progranning "
# a=r.maketrans("n",'m',)
# print(a,type(a))
# print(r.translate(a))
# 
# r={}
# print(r,type(r))
# v={1:'hello', 2:'python'}
# print(v[2])

# a="hello\nCore Python\nProgramming"
# print(a)
# g=a.splitlines()
# print(g,type(g))
# print(g[0])
# print(g[1])
# 
# h="hello corepython programming"
# w=h.split()
# print(w,type(w))
# print(w[::-1])
# print(w[1][::-1])

# h="HelloWelcome to Josh Innovations"
# print(h.split(" "))
# print(h.split())
# print(h.split("@"))

# a=2.2,9
# print(a,type(a))

# a=[int(x) for x in input().split()]
# print(a,type(a))
# print(sum(a))
# print("The sum is"+' '+str(sum(a)))
# print("The sum is",sum(a))

# v="Hello Welcome to JoshInnovations"
# print(v.split())

# b="Hello:Welcome: To:Josh:Innovations"
# print(b.split(":"))

# n="Python#C#Java#R#Dart"
# print(n.split("#"))

# v=r"hello\bollywood"
# print(v,type(v))

# k="Hello!\nWelcome to \nJoshInnovations"
# print(k.splitlines())
# 
# y="Hello!\nWelcome to \nJoshInnovations"
# print(y.splitlines(True))
# 
# f="hello"
# print(f.zfill(7))
# 
# j="Hey! How are you Doing?"
# print(j.partition("are"))

# t="Hey! How are you Doing?"
# r=t.partition("you")
# print(r)
# print(r[0])

# m="We are Learning Python Programming , Python is Basic need \
#  for ML,DS,AI,DL,BigData..etc"
# print(m.partition("Python"))
# print(m.rpartition("Python"))
# 
# c="Python"
# print(c.ljust(8),"Programming Basics")

# x="Python"
# print(x.rjust(8),"Programming Basics")

# z="shainaz"
# print(z.rjust(10,'b'))

# s="shainaz"
# print(s.ljust(10,'b'))

# print(dir(str))