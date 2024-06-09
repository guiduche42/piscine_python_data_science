#$>python tester.py | cat -e
#Nothing: None <class 'NoneType'>$ >> NOT WORKING. class is not correct
#Cheese: nan <class 'float'>$
#Zero: 0 <class 'int'>$
#Empty: <class 'str'>$
#Fake: False <class 'bool'>$
#Type not Found$
#1$
#$>

def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing:", object, type(object), sep=' ')
	elif type(object) is float:
		print("Cheese:", object, type(object), sep=' ')
	elif type(object) is int:
		print("Zero:", object, type(object), sep=' ')
	elif type(object) is str:
		if object == '':
			print("Empty:", object, type(object), sep=' ')
		else:
			print("Type not Found")
	elif type(object) is bool:
		print("Fake:", object, type(object), sep=' ')
	else:
		print("Type not Found")
	return 1
