ab={
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.com',
    'Mali':'mali@qq.com',
    'Spa':'spa@hotmail.com'
}
print('Swaroop \'s address is ',ab['Swaroop'])

del ab['Spa']
print('\nThere are{}contents in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))
    
ab['Guido']='guido@python.org'
if 'Guido' in ab:
    print('\nGuido\'s address is',ab['Guido'])