#$>python tester.py | cat -e
#List : <class 'list'>$
#Tuple : <class 'tuple'>$
#Set : <class 'set'>$
#Dict : <class 'dict'>$
#Brian is in the kitchen : <class 'str'>$
#Toto is in the kitchen : <class 'str'>$
#Type not found$
#42$
#$>

def all_thing_is_obj(object: any) -> int:
	if type(object) == str:
		print(object, "is in the kitchen", ":", type(object), sep=' ')
	elif type(object) == list:
		print("List :", type(object))
	elif type(object) == tuple:
		print("Tuple :", type(object))
	elif type(object) == set:
		print("Set :", type(object))
	elif type(object) == dict:
		print("Dict :", type(object))
	else:
		print("Type not found")
	return 42
