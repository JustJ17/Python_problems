import time
import functools

class Vehicle:

    totalvehicles = 0

    def __init__(self, vehicle_id , brand , model , rental_price_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented = False
        self.totalvehicles += 1
    
    def rent(self):
        if self.is_rented == False:
            self.is_rented = True
            print("this vehicle is now rented")
        else:
            print("this vehicle is already rented")

    def return_vehicle(self):
        if self.is_rented == True:
            self.is_rented = False
            print("this vehicle is now returned")
        else:
            print("this vehicle is not rented")

    def calculate_rental_cost(self,days):
        return days * self.rental_price_per_day

    def get_details(self):
        return f"""Car details: {self.brand} - {self.model}
ID : {self.vehicle_id}  -  ${self.rental_price_per_day}/day -- {'Not Available' if self.is_rented else 'Available'}
                """

class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price_per_day, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.num_doors = num_doors
        Vehicle.totalvehicles += 1
    
    def get_details(self):
        return f"""vehicle details: {self.brand} - {self.model} - Number of doors: {self.num_doors}
ID : {self.vehicle_id}  -  ${self.rental_price_per_day}/day -- {'Not Available' if self.is_rented else 'Available'}
                """
   
class Motorcycle(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price_per_day, engine_cc):
        super().__init__(vehicle_id, brand, model, rental_price_per_day*0.7)
        self.engine_cc = engine_cc
        Vehicle.totalvehicles += 1

    
    def get_details(self):
        return f"""Motorcycle details: {self.brand} - {self.model} - engine cc: {self.engine_cc}
ID : {self.vehicle_id}  -  ${self.rental_price_per_day}/day -- {'Not Available' if self.is_rented else 'Available'}
                """

class Truck(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price_per_day , cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rental_price_per_day*1.5)
        self.cargo_capacity_tons = cargo_capacity_tons
        Vehicle.totalvehicles += 1
    
    def get_details(self):
        return f"""Truck details: {self.brand} - {self.model} - capacity in tons: {self.cargo_capacity_tons}
ID : {self.vehicle_id}  -  ${self.rental_price_per_day}/day -- {'Not Available' if self.is_rented else 'Available'}
                """
    
def test_vehicles():
    car = Car("V001", "Toyota", "Camry", 50, 4)
    motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
    truck = Truck("V003", "Ford", "F-150", 80, 2.5)
    car.rent()
    print(car.is_rented)
    cost = car.calculate_rental_cost(5)
    print(f"Rental cost for 5 days: ${cost}")
    print(motorcycle.get_details())
    car.rent()
    car.rent()
    car.return_vehicle()
    print(car.is_rented)

    print(f"Total vehicles: {Vehicle.totalvehicles}")

class CustomRange:

    def __init__(self, start=0, stop=None, step=1):
        if stop == None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start


    def __iter__(self):
            
            return self

    def __next__(self):
        if(self.current >= self.stop and self.step > 0) or (self.current <= self.stop and self.step < 0):
            raise StopIteration
        else:
            currentVal = self.current
            self.current += self.step
            return currentVal
    def reset(self):
        self.current = self.start

class EvenNumbers(CustomRange):

    def __next__(self):
        while True:
            value = super().__next__()
            if value%2 == 0:
                return value

def customRangeTester():
    resetonce= True
    range=CustomRange(0,10,1)
    for n in range:
        print(n)
        if(n == 5 and resetonce):
            range.reset()
            resetonce = False

def read_file_lines(filename):
    try:
        with open (filename , 'r') as file:
            for line in file:
                yield f"{line}"

    except FileNotFoundError:
        print("the file name was not found!")
    
def filter_lines(lines, keyword):
    for line in lines:
        if line.find(keyword) != -1:
            yield line

def strip_lines(lines):
    for line in lines:
        yield line.strip()

def number_lines(lines):
    i = 1
    for line in lines:
        yield f"{i}.{line}"
        i+=1

def chunk_lines(lines, chunk_size):
    chunk = list()
    for line in lines:
        if len(chunk) < chunk_size:
            chunk.append(line)
        else:
            yield chunk
            chunk.clear()
            chunk.append(line)
    if chunk:
        yield chunk

def timer(function):
    @functools.wraps(function)
    def wrapper(*args , **kwargs):
        start = time.time()
        function(*args , **kwargs)
        total_time = time.time() - start
        print(f"[Timer Function]: the {function.__name__} function executed in {total_time:.4f} seconds")
    return wrapper

def logger(function):
    @functools.wraps(function)
    def wrapper(*args , **kwargs):
        print(f"Calling function {function.__name__} with args = {args} and kwargs = {kwargs} ")
        result = function(*args , **kwargs)
        print(f"Function {function.__name__} returned : {result}")
        return result
    return wrapper

def count_calls(function):
    @functools.wraps(function)
    def wrapper(*args , **kwargs):
        result = function(*args , **kwargs)
        wrapper.counter+=1
        return result
    wrapper.counter = 0
    return wrapper

def debug(function):
    @functools.wraps(function)
    def wrapper(*args , **kwargs):
        print(f"[Debug]: Calling function {function.__name__}")
        print(f"[Debug]: Args = {args}")
        print(f"[Debug]: Kwargs = {kwargs}")
        result = function(*args , **kwargs)
        print(f"[Debug]: {function.__name__} returned : {result}]")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)
    return f"Slept for {n} seconds"

@logger
def add(a, b):
    return a + b

@count_calls
def greet(name):
    return f"Hello, {name}!"

@debug
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

@timer
@logger
def multiply(x, y):
    return x * y

def decorators_test():
    result = slow_function(2)
    print(result)

    result = add(1,2)
    print(result)

    greet("Moahmed")
    greet("Ahmed")
    greet("Yahia")
    print(greet.counter)

    calculate_average([1,2,3,4])

    multiply(3,7)

class Product:
    def __init__(self,product_id , name , price , stock , category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def add_stock(self, stock):
        self.stock += stock

    
    def reduce_stock():
    
    def apply_discount(percentage):

class Review:
    pass

class ProductWithReviews(Product):
    pass

class ShoppingCart:
    pass