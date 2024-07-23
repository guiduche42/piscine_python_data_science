from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!", "titi"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(22)
all_thing_is_obj("Faut il inclure 42")
all_thing_is_obj("Myriam ne sait pas")
print(all_thing_is_obj(ft_tuple))
