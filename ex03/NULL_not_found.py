#$>python tester.py | cat -e
#Nothing: None <class 'NoneType'>$
#Cheese: nan <class 'float'>$
#Zero: 0 <class 'int'>$
#Empty: <class 'str'>$
#Fake: False <class 'bool'>$
#Type not Found$
#1$
#$>

def NULL_not_found(object: any) -> int:
	if type(object) == None:
		print("Nothing:", object, type(object), sep=' ')
	elif type(object) == float:
		print("Cheese:", object, type(object), sep=' ')
	elif type(object) == int:
		print("Zero:", object, type(object), sep=' ')
	elif type(object) == str:
		print("Empty:", object, type(object), sep=' ')
	elif type(object) == bool:
		print("Fake:", object, type(object), sep=' ')
	else:
		print("Type not Found")
	return 1
