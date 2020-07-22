import datetime
import time

NUM_REQUESTS_ALLOWED = 5

def test():
    data = {}
    # data = request(data, 2 )
    # data = request(data, 2 )
    # data = request(data, 2 )
    
    
    print(my_rate_limited_api(data, 1)) # True 2
    print(my_rate_limited_api(data, 1)) # True 3
    print(my_rate_limited_api(data, 1))# True 4
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 2))
    print(my_rate_limited_api(data, 1)) # True 
    print(my_rate_limited_api(data, 1)) # False
    print(my_rate_limited_api(data, 1))
    print(my_rate_limited_api(data, 2))
    
    time.sleep(1)
    
    print(my_rate_limited_api(data, 1))
    print(my_rate_limited_api(data, 1))
    return my_rate_limited_api(data, 1)
    

def my_rate_limited_api(data, user_id):
    if rate_limited(data, user_id):
        request(data, user_id)
    else:
        return False
    
    
def rate_limited(data, user_id):
    counter = 0
    
    end_time = datetime.datetime.now()
    start_time = datetime.datetime.now() - datetime.timedelta(seconds=1)
    
    counter += get_num_requests(data, user_id, start_time, end_time)
    
    if counter > NUM_REQUESTS_ALLOWED - 1:
        return False
    
    return True
    
def get_num_requests(data, user_id, start_time, end_time):
    counter = 0
    if user_id not in data:
        data[user_id] = []
    for data_elem in data[user_id]:
        if start_time <= data_elem['time'] and data_elem['time'] <= end_time:
            counter += 1
    return counter
    
def create_data():
    data = {}
    data[1] = [
        {
        'time': datetime.datetime.now(),
        'type': 'GET'
        },
        {
        'time': datetime.datetime.now(),
        'type': 'GET'
        }, 
        {
        'time': datetime.datetime.now(),
        'type': 'GET'
        }
        
        
    ]
    return data
    
def request(data, user_id):
    data[user_id].append({
        'time': datetime.datetime.now(),
        'type' :' GET'
    })
    return data
    

print(test())

# Keep track of all the items in our store
#  name
#  price
# Keep track of all the purchases that have been made
#  items
#  totalcost
#  time
#  name of person


# class Item():
#     name = None
#     def __init__(self, name):
#         self.name = name

# class Storage():
#     # list of items 
#     items = None
#     def __init__(self, items):
#         self.items = items
    
# class Item():
#     name = None
#     def __init__(self, name, price, number_available):
#         self.name = name
#         self.price = price
#         self.number_purchased = number_available

# class OrderedItem(Item):
#     def __init__(self, item, number_ordered):
#         self.name = item.name
#         self.price = item.price
#         self.number_ordered = number_ordered

# class Purchase():
    
#     def __init__(self, time, person, items):
#         self.time = time
#         self.person = person
#         self.items = items
#         self.totalcost = 0
        
#         # self.purchase = dict()
#         # items shampoo price number 
        
    
#     def get_totalcost(self, items):
#         for item in items:
#             if item.number_ordered > 0 :
#                 self.totalcost = self.totalcost + item.price*item.number_ordered
#         return self.totalcost

# shampoo = Item("Shampoo", 500, 5)
# conditioner = Item("Conditioner", 800, 1)
# soap = Item("Soap", 200, 5)

# items = [OrderedItem(shampoo, 2), OrderedItem(conditioner, 1), OrderedItem(soap , 1)]

# purchase = Purchase('July 5 6pm', 'Hikari', items)
# print(purchase.get_totalcost(items))


# public class Class{
#     static void has_sum_to_k(int[] list, int sum){
#         int remain = k;
#         // 1234 4 
#         Set<Integer> set = new HashSet<Integer>(); 
#         for (int x : list) 
#             set.add(x); 
#         // print(set)
#         // for(int i = 0; i < list.length(); i++){
#         //     list[i]
#         // }
        
#     }
    
#     public static void main(String[] args) {
#         has_sum_to_k([1,2,3,4,1,2,3,4,5,5], 4);
#     }
# }

# def has_sum_to_k(numbers, sum_num):
#     remain = sum_num
#     # numbers = sorted(numbers)
#     numbers.sort()
#     pointer1 = 0
#     pointer2 = len(numbers) - 1
    
#     while(pointer1 < len(numbers) and pointer2 > 0):
#         sum_temp = numbers[pointer1] + numbers[pointer2]
#         if sum_temp == sum_num:
#             return True
#         elif sum_temp > sum_num:
#             pointer2 = pointer2 -1
#         else:
#             pointer1 = pointer1 + 1
            
#     return False        
    
# print(has_sum_to_k([1,2,3,4,0,1,-2,125], -2))
