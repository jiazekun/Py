print('Simple Assignment')
shoplist=['apple','mango','banana']
mylist=shoplist
del shoplist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)

print('Copy bymaking a full slice')
mylist=shoplist[:]
del mylist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)