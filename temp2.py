# class Customer:

#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     @staticmethod
#     def check_type(value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Банк работает только с числами')
    
#     def withdraw(self, value):


# def skat(n): 
#     """Функция, которая возвращает последовательность от 0 до n""" 
#     # сознательно не используем тут range, потому как range является объектом-итератором.
#     res = []
#     cnt = 0
#     while cnt < n:
#         res.append(cnt)
#         cnt += 1
#     return res

# def first_eater(eda_list): 
#     """Первый подопытный""" 
#     for eda in eda_list: 
#         print(f"Первый подопытный съел {eda} и написал: ", str(eda)) 
      
      
# def second_eater(eda_list): 
#     """Второй подопытный""" 
#     for eda in eda_list: 
#         print(f"Второй подопытный съел {eda} и написал: ", str(eda) * 4) 
      
      
# def third_eater(eda_list): 
#     """Третий подопытный""" 
#     for eda in eda_list: 
#         print(f"Третий подопытный съел {eda} и написал: ", str(eda) * 10)
      
      
# # заряжаем скатерть
# eda_list = skat(100_000_000) 
# # задаём параметры голода
# golod_1 = 2 
# golod_2 = 3 
# golod_3 = 4 
# # кормим
# # first_eater(eda_list[:golod_1])
# # second_eater(eda_list[golod_1:golod_2 + golod_1])
# # third_eater(eda_list[golod_2 + golod_1:golod_2 + golod_1 + golod_3])
# print(eda_list[:golod_1])


import sqlite3

try:
    con = sqlite3.connect("mydb.sqlite")
except sqlite3.Error as er:
    print("Error connecting to database:", er)

cur = con.cursor()
sql_query = "INSERT INTO user VALUES(?, ?)"
sql_data = ("John", "MacDonald")

try:
    cur.execute(sql_query, sql_data)
    con.commit()
except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
finally:
    con.close()