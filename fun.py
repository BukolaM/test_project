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

    
def car_revenue(d): 

    e = get_unique_cars(d) 

    print(e)

    prepare_list = prepare(e)

    return prepare_list


a = get_csv('Data/New_Data.csv')
# print(a)


y = car_revenue(a)
# print(y)


def square(e):
    c = e * e
    return c

def sum_square(a, b):
    d = square(a)
    c = a + b + d
    return c

def minus_square(a, b):
    d = square(a)
    c = a + b - d
    return c

# x = sum_square(2, 1)
# print(x)

# x = minus_square(2, 1)
# print(x)

# c = square(5)
# print(c)










