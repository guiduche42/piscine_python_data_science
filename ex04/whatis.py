import sys

def is_integer(s):
	# Check if the string is a valid integer
	if s.isdigit():
		return True
	elif s.startswith('-') and s[1:].isdigit():
		return True
	return False

def whatis():
	if len(sys.argv) == 1:
		return
	try:
		# Check if exactly one argument is provided
		assert len(sys.argv[1:]) == 1, "more than one argument is provided"
		assert is_integer(sys.argv[1]), "argument is not an integer"
		arg = int(sys.argv[1])
		if arg % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except AssertionError as e:
		print(f"AssertionError: {e}")

if __name__ == "__main__":
	whatis()