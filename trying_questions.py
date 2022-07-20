
orders = [
    {
        'customer': 'Anita',
        'pickup':'ikeja',
        'destination':'vi',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'October'
    },
    {
        'customer': 'Mary',
        'pickup':'ogba',
        'destination':'bariga',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'July'
    },
    {
        'customer': 'Kola',
        'pickup':'badagri',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'May'
    },
    {
        'customer': 'Kola',
        'pickup':'VI',
        'destination':'Mende',
        'amount': 2500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'December'
    },
     {
        'customer': 'Mary',
        'pickup':'Ikorodu',
        'destination':'Ogba',
        'amount': 1500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'December'
    },
     {
        'customer': 'Victor',
        'pickup':'Yaba',
        'destination':'Oyinbo',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'Febuary'
    },
    {
        'customer': 'Anita',
        'pickup':'Yaba',
        'destination':'Oyinbo',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'August'
    },
     {
        'customer': 'Victor',
        'pickup':'VI',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'Sepetember'
    },
     {
        'customer': 'Mary',
        'pickup':'Ojota',
        'destination':'Sabo',
        'amount': 3500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'Sepetember'
    },
     {
        'customer': 'Tosin',
        'pickup':'Ketu',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'Febuary'
    },
     {
        'customer': 'Mary',
        'pickup':'Ikorodu',
        'destination':'VI',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'July'
    },
     {
        'customer': 'Mary',
        'pickup':'Ojota',
        'destination':'Maryland',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'May'
    },
    {
        'customer': 'Victor',
        'pickup':'Mowe',
        'destination':'Sabo',
        'amount': 10500,
        'status':'pending',
        'paymentMode' :'transfer',
        'month': 'March'

    },
     {
        'customer': 'Bola',
        'pickup':'Ogba',
        'destination':'Ikorodu',
        'amount': 500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'January'
    },
     {
        'customer': 'Anita',
        'pickup':'VI',
        'destination':'Sabo',
        'amount': 1500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'January'
    }
]



  



#-------------------------------------------unique customer's total count
##customer with the highest order in tersm of count
# unique_customer=[]
for order in orders:
    print(order['customer'])
#     if order['customer'] not in unique_customer:
#         unique_customer.append(order['customer'])
# print(unique_customer)

# # ##inputting this list into a dict
# # revenue_count={}
# # for key_customer in unique_customer:
# #   revenue_count[key_customer]=0
# # print(revenue_count)


# # ##to get the actual customer's count
# # for order in orders:
# #         customers= order['customer']
# #         revenue_count[customers]=revenue_count[customers] +1
# # print(revenue_count)

# ##customer's revenue'-----------------------------------------------------
# # unique_customers=[]
# # unique_customers_revenue={}
# # for order in orders:
# #     if order['customer'] not in unique_customers:
# #         unique_customers.append(order['customer'])


# # for m in unique_customers:
# #     print(m)
# #     unique_customers_revenue[m]=0


for order in orders:
    key=order['customer']
    print(key)
    value=unique_customers_revenue[key] + order['amount']
    unique_customers_revenue[key]=value

    print(unique_customers_revenue[key])
    
# # print(unique_customers_revenue)
# #---------------------------------------------------------------------------
# # to get count of payment mode
# # payment_mode=[]
# # for order in orders:
# #     if order['paymentMode'] not in payment_mode:
# #         payment_mode.append(order['paymentMode'])

# # all_payment={}
# # index=0
# # for payment in payment_mode:
# #     all_payment[payment]=0
# # print (all_payment)


# # for order in orders:
# #     key=order['paymentMode']
# #     value= all_payment[key] + order['amount']
# #     # all_payment[key]=all_payment[key] + 1   or 
# #     all_payment[key]= value
# # print(all_payment)





# ##defining a function for unique customer----------------------------------------------
# # def all_menu(x):
# #     unique_menu=[]
# #     for numbers in x:
# #         if numbers not in unique_menu:
# #             unique_menu.append(numbers)
# #     return unique_menu




# # print(y)
# ##using a function to get revenue--------------------------------------------------------------------------------------------
# # def get_unique_menu(x):
# #     unique_menu=[]
# #     for numbers in x:
# #         if numbers['food'] not in unique_menu:
# #             unique_menu.append(numbers['food'])
# #     return unique_menu


# # def prepare_revenue(unique_menu):
# #     all_revenue={}
# #     for customer in unique_menu:
# #         all_revenue[customer]=0
# #     return all_revenue



# # def menu_revenue(x):
# #     unique_menu= get_unique_menu(x)
    
# #     all_revenue= prepare_revenue(unique_menu)
    
  
# #     for numbers in x:
# #         key = numbers['food']
# #         value = all_revenue[key] + numbers['price']
# #         all_revenue[key]=value
# #     return all_revenue



# # def menu_count(x):
# #     unique_menu= get_unique_menu(x)
    
# #     all_revenue= prepare_revenue(unique_menu)
  

# #     for numbers in x:
# #         key = numbers['food']  
# #         all_revenue[key]=all_revenue[key] +1

# #     return all_revenue


# # menus = [{'food':'breakfast','time':'8am','price':5000, 'restaurant':'gilab', 'tranferred':'no'},
# # {'food':'lunch','time':'2pm','price':5000, 'restaurant':'the place', 'tranferred':'no'},
# # {'food':'dinner','time':'9pm','price':3000, 'restaurant':'roadside', 'tranferred':'yes'},
# # {'food':'breakfast','time':'10am','price':9000, 'restaurant':'dominoes', 'tranferred':'yes'},
# # {'food':'lunch','time':'3pm','price':8000, 'restaurant':'the place', 'tranferred':'no'}]



# # y=menu_count(menus)
# # print(y)
# ##--------------------------------------------------------


# # tosin = "Hello Bukola\nHow are you doing today\nHope you are fine\ni miss you"

# # y = tosin.split("\n")

# # tosin = ['Hi \nBukola', '\ttosin']

# # a = ", ".join(tosin)

# # print(a)

# # # print(y)

# # # print(tosin)

# ##--------------------------------------------------------------------------------------

# all_menu=[{'food':'breakfast','time':'8am','price':5000, 'restaurant':'gilab', 'tranferred':'no'},
# {'food':'lunch','time':'2pm','price':5000, 'restaurant':'the place', 'tranferred':'no'},
# {'food':'dinner','time':'9pm','price':3000, 'restaurant':'roadside', 'tranferred':'yes'},
# {'food':'breakfast','time':'10am','price':9000, 'restaurant':'dominoes', 'tranferred':'yes'},
# {'food':'lunch','time':'3pm','price':8000, 'restaurant':'the place', 'tranferred':'no'}]

# ##to get the unique food
# def menu(y):
#     unique_food=[]
#     for meals in y:
#         if meals['food'] not in unique_food:
#             unique_food.append(meals['food'])
#     return unique_food

# ##to set the price for unique food:

# def total_unique_food_price(c):
#     a = menu(c)
#     unique_food_price={}
    
#     for y in a:
#         unique_food_price[y]=0

#     for all_menus in c:
#         key=all_menus['food']
#         value=unique_food_price[key] + all_menus['price']
#         unique_food_price[key]=value
#     return unique_food_price

# food = total_unique_food_price(all_menu)


# with open('result.txt', 'a+') as file:
#     file.write(food)

# # out = ""

# # for key in food:
# #     out =  out + "The total price of " + key + " is " + str(food[key]) + " and \n"
  
# # print(out)


# # order = {
# #     'name': 'bukola',
# #     'month':'january',
# #     'year':1994,
# #     'age': 28,
# #     'gender':'male',
# #     'country' :'nigeria',
# #     'currency' :'USD',
# #     'salary': 200000
# # }

# # # print (order['name'])

# # for item in order:
# #     print(order[item])
    

# # #     print order

# #     print (key)



