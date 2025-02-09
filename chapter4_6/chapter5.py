# msg = """Hello!
# How are you?
# I'm fine"""
# print(msg)

# print("Hello\nPython\t!!!")

# msg = "Hello"
# print(msg[1])

# msg = "Hello"
# print(msg[1:4])

# msg = "Hello"
# print(msg + "goodby")
# print(msg * 2)
# msg += "!"
# print(msg)

# msg ="Hello"
# for char in msg:
#     print(char)

# msg = "my name is bob"
# name = "bob"
# if(name in msg):
#     print("含まれる")
# else:
#     print("含まれない")

# name ="bob"
# age = 25
# print(f"{name}は{age}才です。")

# print(r"C:\Users\ntaka\hoge.py")

# リスト
# numbers = [10, 20, 30, 40]
# print(numbers)
# print(numbers[2])
# members = ["bob", "tom", "Ivy"]
# print(members)
# members[1] = "tim"
# print(members)

# members = [10, 30, 20]
# print(members[:2])
# print(members + [20])
# print(members * 2)

# numbers = [10, 30, 20, 40]
# # for number in numbers:
# #     print(number)
# if 10 in numbers:
#     print(f"10は{numbers}に含まれる")
# else:
#     print("含まれない")

# numbers = [
#     [10, 30, 20, 40],
#     [11, 31, 21],
#     [12]
# ]
# for row in numbers:
#     for number in row:
#         print(number)

# タプル
# numbers = (10, 30, 20, 40)
# print(numbers)
# members = "Bob", "tom", "ivy"
# print(members)

# numbers = (10, 30, 20)
# (x, y, z) = numbers
# print(f"x:{x},y:{y},z:{z}")
# a,b = "bob", "tom"
# print(f"a:{a},b:{b}")

# members = [("bob", 25), ("tom", 32), ("Ivy", 23)]
# for name, age in members:
#     print(f"名前:{name}, 年齢:{age}")

# 辞書
person = {
    "name": "bob",
    "gender": "male",
    "age": 25
}
# person["age"] += 1
# person["favorite"] = "りんご"
# print(person)
for key in person:
    print(f"{key}: {person[key]}")