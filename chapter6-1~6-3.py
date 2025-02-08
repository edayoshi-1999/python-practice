# 関数
# def get_area(x, y=5):
#     return x * y
# print(get_area(3, 4))
# print(get_area(3))

# def get_area(x=3, y=5):
#     return x * y
# print(get_area())

# def get_area(x=3, y=5):
#     return x * y
# print(get_area(y=3))

# def print_positional_args(*args):
#     print(args)
# print_positional_args(10, 30, 20, 40)
# print_positional_args("tom", "bob")

# def print_keyword_args(**kwards):
#     print(kwards)
# print_keyword_args(name="bob", gender="male", age=24)

# 組み込み関数
# members = ["bob", "tom", "ivy"]
# member = input("メンバー名を入力")
# if member in members:
#     print(f"{member}は{members}の一員です。")
# else:
#     print(f"{member}は{members}ではない。")

# print(dict(name="bob", age=25))
# print(dict({"name":"bob", "age":25}, favorite="apple"))
# print(dict([("name", "bob"), ("age", 25)]))

# members = ["bob", "tom", "ivy"]
# my_iter = iter(members)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# members = ["bob", "tom", "ivy"]
# print(list(enumerate(members)))
# for i, member in enumerate(members): アンパック
#     print(i, member)

# letters = "abc"
# members = ["bob", "tom", "ivy"]
# favorites = ["apple", "banana", "grape"]
# print(list(zip(letters, members, favorites)))
# for letter, member, favorite in zip(letters, members, favorites):
#     print(letter, f"{member}は{favorite}がすきです")

# def mod_five(n):
#     return n % 5
# numbers = [7, 3, 5, 1, 3]
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(sorted(numbers, key=mod_five))

# foods = ["spam", "ham", "bacon"]
# print(sorted(foods))
# print(sorted(foods, reverse=True))
# print(sorted(foods, key=len))

# 式
# my_list =[]
# for i in range(1,21):
#     if i % 3 == 0 or "3" in str(i):
#         my_list += [i]
# print(my_list)
# my_list = [i * 2 for i in range(1,21) if i % 3 == 0 or "3" in str(i)]
# print(my_list)

# members = ["bob", "tom", "ivy"]
# favorites = ["apple", "banana", "grape"]
# actives = [True, False, True]
# my_dict = {}
# for key, value, active in zip(members, favorites, actives):
#     if active:
#         my_dict[key] = value
# print(my_dict)
# my_dict = {
#     key: value 
#     for key, value, active in zip(members, favorites, actives)
#     if active
# }
# print(my_dict)

# gen = (i for i in range(10,20) if i % 3 == 0 or "3" in str(i))
# for x in gen:
#     print(x)
# print(type(gen))
# print(next(gen))