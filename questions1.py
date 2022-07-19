



from re import X


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

# def all_customers(orders):
#     customers=[]
#     for order in orders:
#         if order['customer'] not in customers:
#             customers.append(order['customer'])
#     return customers

# b = all_customers(orders)
# print(b)


# def get_unique_customers(orders):
#     unique_customer=[]
#     for order in orders:
#         if order['customer'] not in unique_customer:
#             unique_customer.append(order['customer'])
#     return unique_customer


# y = get_unique_customers(orders)
# print(y)









# def number(x,y):
#     answer=x**y
#     if answer==0:
#         return 1
#     else:
#         return answer

# k = number (2,4)
# print (k)
































# def get_unique_customers(orders):
#     unique_customer=[]
#     for order in orders:
#         if order['customer'] not in unique_customer:
#             unique_customer.append(order['customer'])
#     return unique_customer


# y = get_unique_customers(orders)
# print(y)












# # print(orders)
# months = []
# for x in orders:
#     if x['month'] not in months:
#         months.append(x['month'])
# # print(months)

# month_rev = {}

# for mon in months:
#     month_rev[mon] = 0

# for y in orders:
#     c = y['month']
#     s = y['amount']

#     month_rev[c] = month_rev[c] + s
    

# print(month_rev)





## What is the total number of orders
# orders_count= len(orders)
# print(orders_count) 

# all_orders=0
# for order in orders:
#     all_orders=all_orders+ 1
# print(all_orders)


## What is the total number of orders per month
# month_order_count=[]
# for order in orders:
#     if order['month'] not in month_order_count:
#         month_order_count.append(order['month'])
# # # count_order=len(month_order_count)
# # # print(count_order)


# month_order_count=[]
# for order in orders:
#     if order['month'] not in month_order_count:
#         month_order_count.append(order['month'])
# count_order_month=0
# for total in month_order_count:
#     count_order_month=count_order_month +1
# print(count_order_month)

# unique_month={}
# for mot in month_order_count:
#     unique_month[mot]=0
# print(unique_month)


# for order in orders:
#     m=order['month']
#     amount=order['amount']
#     print(amount)
#     unique_month[m]= unique_month[m] + amount








## What is the total revenue per month

## list out your unique customer
# unique_customer=[]
# for person in orders:
#     if person['customer'] not in unique_customer:
#         unique_customer.append(person['customer'])
# print(unique_customer)
# print(len(unique_customer))


# unique_customer=[]
# for person in orders:
#     if person['customer'] not in unique_customer:
#         unique_customer.append(person['customer'])
# print(unique_customer)
# cus= 0
# for cust in unique_customer:
#     cus= cus + 1
# print(cus)

# total_revenue={}
# for name in unique_customer:
#     print(name)
#     total_revenue[name]=0
# print(total_revenue)

# for person in orders:
#     # n= person['customer']
#     # rev= person['amount']
#     # total_revenue[n]=   total_revenue[n] + rev
#     total_revenue[person['customer']] = total_revenue[person['customer']] + person['amount']

# print(total_revenue)















## How many order came from each customer
# unique_customer=[]
# for order in orders:
#     if order['customer'] not in unique_customer:
#         unique_customer.append(order['customer'])
# print(unique_customer)


# customer_order={}
# for customers in unique_customer:
#     customer_order[customers]=0
# print(customer_order)

# for order in orders:
#     cus_name=order['customer']
#     customer_order[cus_name] =  customer_order[cus_name] + 1
# print(customer_order)
 
## What is the total revenue per customer

## What is the total order per the status
# order_status=[]
# for order in orders:
#     if order['status'] not in order_status:
#             order_status.append(order['status'])


# status_count={}
# for orders_status in order_status:
#     m = {orders_status:0}
#     status_count.update(m)
#     # print (m)
# print(status_count)


# for order in orders:
#     sts=order['status']
#     status_count[sts]= status_count[sts] +1
# print(status_count)






































## What is the total revenue made

## What is the total revenue per payment mode
# unique_payment_mode=[]
# for order in orders:
#     if order['paymentMode'] not in unique_payment_mode:
#         unique_payment_mode.append(order['paymentMode'])

# total_revenue={}
# for rev in unique_payment_mode:
#     total_revenue[rev]=0
# print(total_revenue)

# for order in orders:
#     paymentMode=order['paymentMode']
#     amount=order['amount']
#     total_revenue[paymentMode]= total_revenue[paymentMode] +  amount
# print(total_revenue)










#revenue per customer
# # to get unique customers
# unique_customers=get_unique_customers(orders)
# # for order in orders:
# #   if order['customer'] not in unique_customers:
# #     unique_customers.append(order['customer'])
# # print(unique_customers)
# print(unique_customers)

# customers={}
# for y in unique_customers:
#     customers[y]=0
# print(customers)

# for order in orders:
#     customer_name=order['customer']
#     customer_revenue = order['amount']
#     customers[customer_name]=customers[customer_name] + customer_revenue

# print(customers)




# x=[2,3,4,5,6,7,8]
# x_square=[]

# for numb in x:
#     numb=numb**2
#     print(numb)
#     x_square.append(numb)
  
# print(x_square)


# x=[2,3,4,5,-1,-9,4,-7,0]
# positive_int=[]
# negative_int=[]

# for numbers in x:
#     print(numbers)
#     if numbers>0:
#         positive_int.append(numbers)
#     else:
#         negative_int.append(numbers)
# print(positive_int)
# print(negative_int)



# dic={'val1':10,'val2':20,'val3':30,'val4':40}
# for x in dic:
#     print(x)
 
# dic1={}
# dic1[x]=0
#     print(dic1)


##Define a function which counts vowels and consonant in a word.

# lists='pythonlobby'
# vow=['a','e','i','o','u']
# count=0
# for list in lists:
#     if list in vow:
#         count=count+1
# print(count)
   

##Make a Python function that takes x as argument and returns y. Call the function for x=2 and print the answer
# def my_func(x):
#     return x

# y = my_func(2)
# print(y)



##Write a function called fizz_buzz that takes a number.
##If the number is divisible by 3, it should return “Fizz”.
##If it is divisible by 5, it should return “Buzz”.
##If it is divisible by both 3 and 5, it should return “FizzBuzz”.
##Otherwise, it should return the same number

def fizz_buzz(x):
    divide_by_3 = False
    divide_by_5 = False
    if x % 3 == 0:
       divide_by_3 = True
    if x % 5 == 0:
        divide_by_5 = True
    if divide_by_3 == True and divide_by_5 == True:
        return 'fizzbuzz'
    elif divide_by_3 == True:
        return 'fizz'
    elif divide_by_5 == True:
        return 'buzz'
    else:
        return x
y= fizz_buzz(30)
print(y)