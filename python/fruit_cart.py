# Write code below 💖
my_set = {'apple','oranges','watermelon','cantaloupe','pomegranate','plum'}
bae_set = {'banana','apple','pears','plum','mango','strawberry','watermelon'}

our_fruit = my_set.union(bae_set)
print(our_fruit)

shopping_list = my_set.intersection(bae_set)
print(shopping_list)

maybe_list = my_set.difference(bae_set)
print(maybe_list)

print('coconut' in our_fruit)
our_fruit.add('coconut')
print(bae_set)
print(our_fruit)
shopping_list.add('lime')
print(shopping_list)
