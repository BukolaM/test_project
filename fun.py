def prepare_result(header, rows):
    result = {}
    index = 0
    for item in header:
        key = item
        value = rows[index]
        result[key] = value
        index = index + 1
    return result

def get_csv(file_path):
    result = []
    with open (file_path) as file:
        c = file.read()
        c = c.split('\n')
        header = c[0]
        header = header.split(',')
        del c[0]
        for rows in c:  
            rows = rows.split(',')
            data = {}
            index = 0
            for item in header:
                key = item
                value = rows[index]
                data[key]=value
                index = index+ 1
            result.append(data)
        return result

def get_unique_cars(cars):

    result=[]
    for unique in cars:
        if unique['make'] not in result:
            result.append(unique['make'])
    return result

def prepare (cars):
    prepare_list={}
    for car in cars:
        key=car
        prepare_list[key]=0
    return prepare_list

    
def car_revenue(cars):  
    prepare_list={}
    unique_car = get_unique_cars(cars) 
    print (unique_car)

    prepare_list = prepare(unique_car)

    for car in cars:
        key=car['make']
        prepare_list[key] = prepare_list[key] + int(car['price'])
    return prepare_list






def back():
    return 'back'
def jump():
    return 'jump'
def come():
    a= jump()
    
    b = back()
    return a + b
 
a=come ()
print(a)






all_cars = get_csv('Data/New_Data.csv')
# # a= get_unique_cars(all_cars)
# # print(a)
# y= car_revenue(all_cars)


unique_car = get_unique_cars(all_cars) 
print (unique_car)

prepare_list={}
for car in unique_car:
    key=car
    prepare_list[key]=0

for car in all_cars:
    key=car['make']
    prepare_list[key] = prepare_list[key] + int(car['price'])
print (prepare_list)










