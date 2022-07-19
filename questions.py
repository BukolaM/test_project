from readline import append_history_file


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

# save the information of all the unique males in this list
males = []

# for person in people:
#     if person['gender']=='male':
#         males.append(person)
# person = []
# for all_males in males:
#     print(all_males)




## save the information of all the unique females in this list
# females = []
# for person in people:
#     if person['gender']=='female':
#         females.append(person)
# for all_females in females:
#     print(all_females)



## add the  country to this list
# countries = []
# for person in people:
#     if person['country'] not in countries:
#         countries.append(person['country']) 
# print(countries)


## What is the total salay paid
# initial_salary= 0
# for person in people:
#     initial_salary=initial_salary+person['salary']
# print(initial_salary)


# Who is the hight paid person
# highest_paid_person = {
#     'salary' : 0
# }

# print(highest_paid_person)
# for person in people:
#     if person['salary'] > highest_paid_person['salary']:
#         highest_paid_person=person

# print(highest_paid_person)


## save the uniqu age in this list
# ages = []
# for person in people:
#     if person['age'] not in ages:
#         ages.append(person['age'])
# print(ages)

# ## What are the unquie months
# months = []
# for person in people:
#     if person['month'] not in months:
#         months.append(person['month'])
# print (months)

## What is the total salary paid per country
# salary_per_country = []
# countries=[]
# for person in people:
#     if person['country'] not in countries:
#         countries.append(person['country'])

# country_salary = {}
# for country in countries:
#     country_salary[country] = 0

# print(country_salary)

# for person in people:
#     country = person['country']
#     country_salary[country] = country_salary[country] + person['salary']

# print(country_salary)


# countries = ['nigeria', 'ghana', 'togo', 'kenya']

# salaries = {
#     'nigeira' :100000,
#     'ghana' :100000,
#     'togo' :100000
# }

# salaries = {}


# for country in countries:
#     salaries[country] = 0

# print(salaries)


# for person in people:
    
#     country = person['country']
#     salary = person['salary']

#     salaries[country] = salaries[country] + salary

  
# print(salaries)





# ## What is the total salary paid per country
# countries=[]
# for person in people:
#     if person['country'] not in countries:
#         countries.append(person['country'])
# print(countries)


# salaries={}

# for country in countries:
#     salaries[country]=0
    
# for person in people:
#     country=person['country']
#     salary= person['salary']

#     salaries[country]= salaries[country] + salary



# print(salaries)


# genders=[]
# for person in people:
#     if person['gender'] not in genders:
#         genders.append(person['gender'])
    
# print(genders)


# gender_count = {}

# genders = ['male', 'female', 'bisexuall']

# for x in genders:
#     gender_count[x] = 0

# print(gender_count)

# for person in people:
#     ys = person['gender']
#     gender_count[ys] = gender_count[ys]  + 1

# print(gender_count)

    



    
#     gender_count[babe] = gender_count[babe] + 1

# print(gender_count)








# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# d={}
# for dict4 in (dic1,dic2,dic3):
#     d.update(dict4)
# print(d)
##------------------------------------------------------------------------
# colours=["Black", "Red", "Maroon", "Yellow"]
# colour_palate= ["#000000", "#FF0000", "#800000", "#FFFF00"]

# colours_and_their_palate = {}
# index_of_each_item=0

# for color in colours:
#     all_colors=colours[index_of_each_item]
#     all_color_palate_details= colour_palate[index_of_each_item]
#     index_of_each_item=index_of_each_item + 1
#     colours_and_their_palate[all_colors]=all_color_palate_details

# print(colours_and_their_palate)
##----------------------------------------------------------------------------


menu=['kneckered spam','pip pip spam', 'squidy spam', 'squishy spam']
list=[0.5,1.50,2.50,3.50]
menu_list={}
index=0

for m in menu:
    menu_item=m
    list_item=list[index]
    index=index+1
    menu_list[menu_item]=list_item
print(menu_list)












## What is the currency of payment
# currency = []
# for person in people:
#     if person['currency'] not in currency:
#         currency.append(person['currency'])
      
# currency = ','.join(currency)

# print(currency)















































## which gender make the most money


# males=[]
# females=[]
# male_salary=0
# female_salary=0

# hight_paid_gender = {}

# for person in people:
#     if person['gender']=='male':
#        males.append(person)

# for all_males in males:
#     male_salary= male_salary + all_males['salary']

# hight_paid_gender[male_salary] = 'male'

# for person in people:
#     if person['gender']=='female':
#         females.append(person)

# for all_females in females:
#     female_salary=female_salary + all_females['salary']

# hight_paid_gender[female_salary] = 'female'


# higest = max(male_salary, female_salary)
# print(hight_paid_gender[higest])
















































# x=[10,23,24,35,65,78,90]
# # even_numbers=[]
# # odd_numbers=[]
# for numbers in x:
   
#     if numbers%2==0:
#         even_numbers.append(numbers)
#     else:
#         odd_numbers.append(numbers)
# print(even_numbers)
# print(odd_numbers)

# x=[2,3,4,5,6,7,8]
# the_square_of_x_of_even_numbers=[]
# the_square_of_x_of_odd_numbers=[]

# for numbers in x:
#     squared_numbers=numbers**2
#     if squared_numbers%2==0:
#         the_square_of_x_of_even_numbers.append(squared_numbers)
#     else:
#         the_square_of_x_of_odd_numbers.append(squared_numbers)
    
# print(the_square_of_x_of_even_numbers)
# print(the_square_of_x_of_odd_numbers)


# print (people[8])

# i = {'key 1': 200, 'key 2':300}

# print (i)

# dict1 = [{'key 1': 200, 'key 2':300}, {'key 1': 200, 'key 2':300}]
# # dict3  = dict1[0]

# # print(dict3)


# initial_salary=0

# for dict in dict1:
#     initial_salary = initial_salary + dict['key 1'] + dict['key 2']

# print(initial_salary)

# print(people[0])


# count = 0
# for person in people:

#     # print("year", person['year'])
#     #####
#     print('person -----> ', person)
#     print('people ----->', people[count])

  
#     count = count + 1
#     # #####



#     x = 2 + 3
#     print (x)

#     print('count', count)

# x=[2,3,4,5,6,7,8]
# the_square_of_x_of_even_numbers=[]
# the_square_of_x_of_odd_numbers=[]


# for numbers in x:
#     the_square_of_x=numbers**2
#     if numbers%2==0:
#         the_square_of_x_of_even_numbers.append(the_square_of_x)
#     else:
#         print(numbers)
#         the_square_of_x_of_odd_numbers.append(the_square_of_x)
# print(the_square_of_x_of_even_numbers)
# print(the_square_of_x_of_odd_numbers)



# males = []

# # salary= salary+ males['salary']

# for person in people:
#     if person['gender']=='male':
#         males.append(person)

# # print(males)


# salary=0
# for male in males:
#     salary = salary + male['salary']

# print (salary)


















   

