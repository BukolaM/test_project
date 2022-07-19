


# with open('Data/LOGISTICS.csv') as logistics_data:
#     logistics=logistics_data.read()
 


# my_logistics_details=logistics.split('\n')


# my_header=my_logistics_details[0]

# headers=my_header.split(',')

# del(my_logistics_details[0])
# # print(my_logistics_details)

# for columns in my_logistics_details:
#     all_columns=columns.split(',')
   

#     header_colums_combinations={}
#     index=0


#     for headrs in headers:
#         key = headers[index]
#         value= all_columns[index]
#         header_colums_combinations[key]=value
#         index=index+1 
#         print(header_colums_combinations)
##--------------------------------------------------------------------------------------
# with open ('/Users/bukola/Desktop/my_project/Data/LOGISTICS.csv') as logistics:
#     for go in logistics.readlines():
#         print(go)
##-------------------------------------------------------------------------
# with open ('capital.csv', 'w+') as capital:
#     red= capital.write('he is good')
# print (red)

##-----------------------------------------------------------------------------
# with open ('capital.csv') as capital:
#     for capitals in capital.readlines():
#         print (capitals)

#------------------------------------------------------------------------
# with open ('capital.csv', 'w') as capitale:
#     capitales = capitale.write('we are ready to leave')
#     print(capitales)

##--------------------------------------------------------------------------
# with open ('capital.csv') as capital:
#     for no in capital.readlines():
#         print (no)
 
##--------------------------------------------------------------------------

# with open('/Users/bukola/Desktop/my_project/Data/New_Data.csv') as New_data:
#     my_data=New_data.read()

#     current_data=my_data.split('\n')
    
#     the_headers=current_data[0]
#     headers_= the_headers.split(',')

#     del current_data[0]

#     for all_rows in current_data:
#         current_row= all_rows.split(',')

#         all_rows_and_keys={}
#         index=0
           
#         for keys in headers_:
           
#             key= keys
#             value= current_row[index]
#             index=index+1
#             all_rows_and_keys[key]=value
#         print(all_rows_and_keys)

         
##to get tht dic
# def get_key_value(all_header, all_columns):
#     all_data_and_keys={}
#     index=0
            
#     for headers in all_header:
#         key= headers
#         value= all_columns[index]
#         index=index + 1
#         all_data_and_keys[key]=value

#     return all_data_and_keys


    

def get_csv(file):

    with open (file) as new_data:
        my_data= new_data.read()
        
        all_data=my_data.split('\n')
    

        my_header=all_data[0]
        all_header= my_header.split(',')
    
        del all_data[0]


        result=[]  
        for data in all_data:
            all_columns=data.split(',')

            all_data_and_keys={}
            index=0
                    
            for headers in all_header:
                key= headers
                value= all_columns[index]
                index=index + 1
                all_data_and_keys[key]=value
            
            result.append(all_data_and_keys)
            
            
        return result




def get_unique_cars(car):
    unique_cars=[]
    for unique in car:
        if unique['make'] not in unique_cars:
            unique_cars.append(unique['make'])
    return unique_cars

cars=get_csv('/Users/bukola/Desktop/my_project/Data/New_Data.csv')


    


x= get_unique_cars(cars)
print (x)

    
       
       
       
       
       
     
    