# def prepare_result(header, rows):
#     result = {}
#     index = 0
#     for item in header:
#         key = item
#         value = rows[index]
#         result[key] = value
#         index = index + 1
#     return result

# def get_csv(file_path):
#     result = []
#     with open (file_path) as file:
#         c = file.read()
#         c = c.split('\n')
#         header = c[0]
#         header = header.split(',')
#         del c[0]
#         for rows in c:  
#             rows = rows.split(',')
#             data = {}
#             index = 0
#             for item in header:
#                 key = item
#                 value = rows[index]
#                 data[key]=value
#                 index = index+ 1
#             result.append(data)
#         return result

# def get_unique_cars(cars):
#     result=[]
#     for unique in cars:
#         if unique['make'] not in result:
#             result.append(unique['make'])
#     return result

# def prepare (cars):
#     prepare_list={}
#     for car in cars:
#         key=car
#         prepare_list[key]=0
#     return prepare_list

    
# def car_revenue(d): 

#     e = get_unique_cars(d) 

#     print(e)

#     prepare_list = prepare(e)

#     return prepare_list


# a = get_csv('Data/New_Data.csv')
# # print(a)


# y = car_revenue(a)
# # print(y)


# def square(e):
#     c = e * e
#     return c

# def sum_square(a, b):
#     d = square(a)
#     c = a + b + d
#     return c

# def minus_square(a, b):
#     d = square(a)
#     c = a + b - d
#     return c

# x = sum_square(2, 1)
# print(x)

# x = minus_square(2, 1)
# print(x)

# c = square(5)
# print(c)










# def unique_food(menus):
#     unique_menus=[]
#     for menu in menus:
#         if menu['food'] not in unique_menus:
#             unique_menus.append(menu['food'])
#     return unique_menus


# def set_values_to_zero(menus):
#     all_menu = unique_food(menus)
#     menu_dict={}
#     for menu in all_menu:
#         key=menu
#         menu_dict[key]=0
#     return menu_dict

# def unique_count(menus):
#     menu_dict=set_values_to_zero(menus)
#     for menu in menus:
#         key= menu['food']
#         menu_dict[key]= menu_dict[key]+1

#     return menu_dict
    



# def unique_restaurant (menus):
#     unique_restau= []
#     for menu in menus:
#         if menu['restaurant'] not in unique_restau:
#             unique_restau.append(menu['restaurant'])
#     return unique_restau

# ## to get the count of the unique restaurant 
# def unique_restaurant_count(menu):
#     unique_count = unique_restaurant(menu)
#     total_count_of_each_restaurant={}
#     for menus in menu:
#         key = menus
#         total_count_of_each_restaurant[key]= total_count_of_each_restaurant[key] + 1
#     return total_count_of_each_restaurant

# x= unique_restaurant_count(all_menu)
# print(x)



# all_menu =[{'food':'breakfast','time':'8am','price':5000, 'restaurant':'gilab', 'tranferred':'no'},
# {'food':'lunch','time':'2pm','price':5000, 'restaurant':'the place', 'tranferred':'no'},
# {'food':'dinner','time':'9pm','price':3000, 'restaurant':'roadside', 'tranferred':'yes'},
# {'food':'dinner','time':'9pm','price':20000, 'restaurant':'roadside', 'tranferred':'yes'},
# {'food':'breakfast','time':'10am','price':9000, 'restaurant':'dominoes', 'tranferred':'yes'},
# {'food':'lunch','time':'3pm','price':8000, 'restaurant':'the place', 'tranferred':'no'}, 
# {'food':'breakfast','time':'8am','price':5000, 'restaurant':'gilab', 'tranferred':'no'}]


# a = 0
# a = a + 1
# a = a + 5
# b = 5

# a = a + b

from mimetypes import init


d = {}

# g = ['a','b','c','d','e','f','g','h']
# # k = ['i','j','k','j','m','n','o','p']

# for key in g:
#     d[key] = 2

# print(d)

# for item in g:
   
#     initial = d[item] 
#     value = 5
#     d[item] = initial + value


# print(d)

data = [
    {'y':'tosin', 'salary': 7000}, 
    {'y':'bukola', 'salary': 4000},
    {'y':'funke', 'salary': 3000},
    {'y':'tosin', 'salary': 2000}, 
    {'y':'bukola', 'salary': 7000},
    {'y':'tosin', 'salary': 6000}, 
    {'y':'bukola', 'salary': 8000},
    {'y':'tosin', 'salary': 3000}, 
    {'y':'bukola', 'salary': 1000},
]

result = {'tosin': 0, 'bukola': 0, 'funke': 0 }

for item in data:
    key = item['y']

    initial = result[key]
    value = initial + 1

    result[key] = value

print(result)

