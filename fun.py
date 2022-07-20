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

def car_revenue(cars):  

    pass


all_cars = get_csv('Data/New_Data.csv')

unique_care = get_unique_cars(all_cars) 










