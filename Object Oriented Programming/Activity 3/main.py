class Crow:

    species = 'bird'

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Crow('Blu', 12)
woo = Crow('Woo', 14)
red = Crow('Red', 17)
green = Crow('Green', 19)

print('Blu is a {}'.format(blu.species))
print('Woo is a {}'.format(woo.species))
print('Green is a {}'.format(green.species))
print('Red is a {}'.format(red.species))


print('{} is {} years old'.format(blu.name , blu.age))
print('{} is {} years old'.format(woo.name , woo.age))
print('{} is {} years old'.format(green.name , red.age))
print('{} is {} years old'.format(red.name , red.age))