import random

def below_than_10(n):
	return n <10

# rand_list =
rand_list = [random.randint(1,20) for _ in range(10)]
# list_comprehension_below_10 =
list_comprehension_below_10 = [ num for num in rand_list if num < 10]
# list_comprehension_below_10 =
list_comprehension_below_10_v2 = filter(below_than_10,rand_list)
print(rand_list)
print(list_comprehension_below_10)
print(list_comprehension_below_10_v2)