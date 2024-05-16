#You need to modify the string of each data object to display the following greetings:
#"Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
#«name of your campus»"

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

ft_list[1] = "World"
ft_tuple = ("Hello", "France")
ft_set.discard("tutu!")
ft_set.add("Paris")
ft_dict["Hello"] = "42Paris"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
