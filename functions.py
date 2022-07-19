


# def bukola(a, b):
#     x = a + 2 - b
#     return x



# def getTosin():
#     return "i love tosin"


# def my_function():
#     print('hello world')

# my_function()



# def my_function(fname):
#   print(fname + " Refsnes")


# my_function('ope')


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")


# def my_function(name, last):
#     print(name, ' ', last)


# my_function('bukola')


# def my_function(foodstuffs):
#     for x in foodstuffs:
#         print(x)




# g=['cake','bread','orange']

# my_function(g)


# g=['g','g','gh']

# my_function(g)






# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# def table(books):
#     for y in books:
#         print (y) 
# tinu=[4,5,6,7]
# table(tinu)


# def my_function(x):
# #   return 5 * x

# # print(my_function(3))
# # print(my_function(5))
# # print(my_function(9))






# # def printme(shout):
# #     x= "This prints the answer"
# #     return x

# # d =  printme('follow')
# # print(d)


# # def my_func():
# # 	x = 10
# # 	print("Value inside function:",x)

# # my_func()


# # def my_funct(a,b):
# #     y=a+b
# #     return y
    
# # a=my_funct(1,2)
# # print (a)


# def calculate_total(height, weight):
#     x= height * weight
#     return x

# b= calculate_total(10,30)
# print('the ans is ' + str(b) + ' now')


# d= calculate_total (1,3)
# print(d)



# def get_even_numbers(numbers):
#     even_numbers=[]
#     for number in numbers:
#         if number%2==0:
#             even_numbers.append(number)
        
#     return even_numbers

# even_numbers=get_even_numbers([2,3,4,5])
# print(even_numbers)



# eve_num=get_even_numbers([5,4,3,2,0,6,8])
# print(eve_num)



# def get_odd_numbers(numbers):
#     odd_numbers=[]
#     for number in numbers:
#         if number%2 != 0:
#             odd_numbers.append(number)
#     return odd_numbers

# odd_numbers= get_odd_numbers([3,9,4,8,0,1])
# print(odd_numbers)



people = [
    {
        'name': 'bukola',
        'month':'january',
        'year':1994,
        'age': 28,
        'gender':'male',
        'country' :'nigeria',
        'currency' :'USD',
        'salary': 200000

    },
    {
        'name':'Anu',
        'month':'febuary',
        'year':1995,
        'age': 26,
        'gender':'female',
        'country' :'ghana',
        'currency' :'USD',
        'salary': 500000
    },
    {
        'name':'Tinu',
        'month':'march',
        'year':1991,
        'age':30,
        'gender':'male',
        'country' :'togo',
        'currency' :'USD',
        'salary': 1000000
    },
    {
        'name':'Bola',
        'month':'june',
        'year':1989,
        'age':32,
        'gender':'male',
        'country' :'togo',
        'currency' :'USD',
        'salary': 600000
    },
     {
        'name':'Remi',
        'month':'june',
        'year':1986,
        'age':35,
        'gender':'female',
        'country' :'kenya',
        'currency' :'USD',
        'salary': 600000
    },
     {
        'name':'Toke',
        'month':'june',
        'year':1990,
        'age':31,
        'gender':'male',
        'country' :'nigeria',
        'currency' :'USD',
        'salary': 450000
    },
    {
        'name':'Victor',
        'month':'august',
        'year':1990,
        'age':31,
        'gender':'male',
        'country' :'togo',
        'currency' :'USD',
        'salary': 1950000
    },
     {
        'name':'Anu',
        'month':'january',
        'year':1989,
        'age':33,
        'gender':'bisexuall',
        'country' :'kenya',
        'currency' :'USD',
        'salary': 120000
    }
]

# ## What is the total salary paid per country
# unique_country=[]
# for person in people:
#     if person['country'] not in unique_country:
#         unique_country.append(person['country'])
# print(unique_country)

# ##to set my unique country to 0
# our_salary={}
# for unique in unique_country:
#    our_salary[unique]=0

# for person in people:
#     original_country=person['country']
#     original_salary=person['salary']
#     our_salary[unique] =our_salary[unique]+1
  
# print[our_salary]

















# c = bukola(10, 2)

# print (c)




# d = getTosin()

# print (d )

# def trip_name(name, origin, destination):
#     print('hello ' + name + ' how are you doing today')
#     print('i hope you are in ' + origin+ ',' + destination)

# trip_name(name=input('enter your name'),origin=input('enter your location'),destination=input('enter your destination'))





# def func():
#     print('the man is known')
# func()


# def my_func(name, place):
#     print ('hello ' + name, ' are you from this '+place)

#     name='bukola'
    
#     place='lagos'

# my_func('name','place')


# def volume_of_cuboid(length,breadth,height):
#   return length*breadth*height

# x=volume_of_cuboid(30,20,10)
# print (x)


# def cube(side):
#   volume = side **3
#   surface_area = 6 * (side**2)
#   return volume, surface_area

# y= cube(3)
# print(y)



# def size(long):
#     volume=long**3
#     area=long**5
#     return volume*area

# k= size(5)
# print(k)




# def my_var_sum(args):
#     total=[]
#     for arg in args:
#         if arg % 2 == 0:
#             total.append(arg)
#     return total
  

  
# l = my_var_sum([2,5,6,8,9])
# print(l)


##Generate a Python list of all the even numbers between 4 to 30


def all_numbers(n):
    even_numbers=[]
    for numbers in n:
        if numbers % 2 != 0:
            even_numbers.append(numbers)
    return even_numbers

    

# a=[2,3,4]
# print(max(a))

# def welcome(project):
#     print('This is my first' + project)

##-----------------------------------------------
# def shut_down(s):
#     if s=='yes':
#         return 'shutting down'
#     elif s=='no':
#         return 'shutdown aborted'
#     else:
#         return 'sorry'

# a = shut_down('no')
# print(a)
##----------------------------------------------

# def distance_from_zero(a):
#     if a==int or float:
#         return abs(a)
#     else:
#         return 'nope'
# y= distance_from_zero(-5.0)
# print(y)

##----------------------------------------------------

# def cube(number):
#     return number**3

# y= cube(5)
# print(y)
##----------------------------------------------------------------------
# def by_three(number):
#     if number%3==0:
#         return number**3
#     else:
#         return 'false'

# a= by_three(9)
# print(a)
##----------------------------------------------------------------------

# def voting_rules(h):
#     for a in h:
#         if a < 18:
#             return 'cannot vote'
#     else:
#         return 'can vote'





# k = voting_rules([30,40,50])
# print (k)


##Python program to display all the multiples of 3 within the range 10 to 50------------------------------
# def multples_of_three(w):
#     all_answers=[]
#     index=0
#     for numbers in w:
#         if numbers%2==0:
#             index=index+1
#             all_answers.append(numbers)
#     return all_answers






# y= multples_of_three(range(10,50))
# print(y)


##----------Python program to generate the prime numbers from 1 to N---------------
def prime_numbers(n):
    all_answers=[]
    for numbers in n:
        if n%2==0:
            all_answers.append(numbers)
    return all_answers

##--------------------------------------------------------------------



# x= range(1,n)
# y= prime_numbers(x)
# print(y)
###----------------------------------------------------------------------

# ##defining th max of three numbers
# def maximum_of_the_numbers(a,b,c):
#     n=[a,b,c]
#     k= max(n)
#     return k
   

   
# y=maximum_of_the_numbers(10,9,6)
# print (y)
##--------------------------------------------------------------

# def maximum(numbers):
#     return max(numbers)
   
# max_var= maximum([10,9,70,4])

# print (max_var)
##------------------------------------------------------------------------------------































##-----------------------------------------------------------------
# name = 'Tosin, Adesipe Babafemi             '

# # print(name)

# # data = name.split(",")

# up = name.upper()

# y =  up.upper().strip() + " good"

# # print(y)
##------------------------------------------------------------------


# name = ['tosin','adesipe','babafemi']

# print(name)

# ne = ","

# # print(ne.join(name))


# food = " hhhhhhh "


# names = ['tosin', 'bukola', 'Mg']

# out = ''

# de = ' , '

# print(de.join(names))
# for name in names:
#     out = out + de + name
#     # print (name)


# print(out)

# print(names)
# r = food.join(name)
# print(r)


##----------------------------------------------------------------------

# total = [1,2]

# total.extend(2)

# print(total)

# u = [1,4,7]

# for x in u:
#     total = total + x

# print(total)


# firstname = data[0]


# print("Hi "+ firstname + "\n\tWelcome to my application ")

# print(data)


# date = '2020-01-12'

# result = date.split("-")

# print (result)

# yesr = result[0]

# month = result[1]

# day = result[2]

# data = ['Tosin', 'Adesipe', 'Babafemi']


# name = ' '.join(data)

# print (name)

##-------------------------------------------------
# name= ' ayo '
# location='yaba, anthony,sabo'
# # # print(location)
# # # x=name.join(location)
# # # print(x)


# y=location.split(',')
# print(y)
##---------------------------------------------------------------

# vehicles=['toyota','volvo','bmw','benz']
# k= ' > '
# h= k.join(vehicles)
# print(h)



# vehicle='toyota, volvo, bmw, benz'
# x= vehicle.split(',')
# print(x)
##------------------------------------------------------------------



def sqaure_numbers (x):
    square_of_numbers = {}
    for y in x:
        square_of_numbers[y] = y*y
    return square_of_numbers

result=sqaure_numbers(range(5,16))
print(result)


places = ['name', 'phone','address']
names = ['funke','08037368261', 'lagos']
result={}
index=0
for place in places:
    key=places[index]
    value=names[index]
    result[key]=value
    index=index+1
print(result)




