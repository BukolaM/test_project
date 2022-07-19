


# result = file.split("\n")



# result = [
#     'name,phone,country,state',
#     'tosin,08037268261,nigeria,lagos', 
#     'bukola,08162132121,usa,maryland', 
#     'fubke,08032229202,usa,washionton'
# ]

# y=result[0]
# print(y)


# x=','
# b=y.split(x)
# print(b)

##-------------------------------------------------------------------------------
# w=['the ','goat ','is ','dead']
# b='>'

# c=b.join(w)
# print(c)

##-------------------------------------------------------------------------------
# name ='the goat is dead, you can carry it,thank you'
# w=','
# p=name.split(w)
# print(p)
##-------------------------------------------------------------------------------


# print
# r=(result[0])

# w=','
# b=r.split(w)
# print(b)


##--------------------------------------------------------------------------------
# result='the man is coming/ please carry the cap'
# print(result)
# a=','
# l=result.split(a)
# print(l)
##------------------------------------------------------------------------------

# file = '''name,phone,country,state
# tosin,08037268261,nigeria,lagos
# bukola,08162132121,usa,maryland
# fubke,08032229202,usa,washionton'''

# print (file)


##-----------------------------------------------------------------------------

# # def get_item(y):
# #     return y.split(',')


# file = '''name,phone,country,state
# tosin,08037268261,nigeria,lagos
# bukola,08162132121,usa,maryland
# fubke,08032229202,usa,washionton'''

# # print(file)

# result = file.split("\n")

# keys = result[0]

# # print(keys)

# keys = keys.split(',')

# del result[0]

# # print(result)

# final = []

# for item in result:
    
#     item = item.split(',')
#     # print(item)

#     response = {}
#     index = 0

#     for x in keys:
#         key = x
#         value = item[index]
#         response[key] = value
#         index = index + 1



#     final.append(response)

# print(final)



# file = '''name,phone,country,state
# tosin,08037268261,nigeria,lagos
# bukola,08162132121,usa,maryland
# fubke,08032229202,usa,washionton'''

# x=file.split('\n')

# the_key_values=x[0]


# the_header_list=the_key_values.split(',')

# del x[0]

# all_list=[]
# for y in x:
#     k = y.split(",")

#     the_result={}
#     index=0
#     for key in the_header_list:
#         keys=key
#         v_alues=k[index]
#         index=index+1
#         the_result[keys]=v_alues
    
#     print(the_result)
#     all_list.append(the_result)
# print(all_list)


##-------------------------------------------------------------------------------------


file = '''CUSTOMER,Price,PAYMENT_MODE,PAYMENT_STATUS,DELIVERY_MODE,Dleivery_Status,Month
Gokada,2300,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1200,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,900,Transfer,confirmed,SHYPES 2,PENDING,Mar
Gokada,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,900,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1300,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1100,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1300,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Ann,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Ann,1500,cash,confirmed,SHYPES 2,DELIVERED,Mar
Ann,1500,cash,confirmed,SHYPES 2,DELIVERED,Mar
Ann,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Ann,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,2300,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1600,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1400,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1100,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1900,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,900,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1200,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1700,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,2700,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1100,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,900,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1300,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1100,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1100,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Gokada,1900,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Abike,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Abike,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Abike,3000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,2000,Transfer,confirmed,SHYPES 2,DELIVERED,Mar
Outsourced,1500,Transfer,confirmed,SHYPES 2,DELIVERED,Mar'''
 
 

# the_list = file.split('\n')

# my_key_values= the_list[0]

# all_my_key_values=my_key_values.split(',')


# del my_key_values
# print(the_list)

# for list in the_list:
#     all_values=(list.split(','))
  
    
#     all_orders={}
#     the_whole_list=[]
#     index=0

#     for key in all_my_key_values:
       
#         keys=key
#         values=all_values[index]
#         index=index+1
#         all_orders[keys]=values
#     print(all_orders)
#     the_whole_list.append(all_orders)

# print(the_whole_list)


# with open("LOGISTICS.csv") as file:
#     index = 0
#     for line in file.readlines():
#         line = line.split(',')
#         print(line)
#         index = index + 1

#         if (index > 2):
#             break
    


