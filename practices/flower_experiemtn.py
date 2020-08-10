# amount
import random

def say_hello():
    print('Hello, World')
    
def simulate_experiments(number_of_experiements):
    all_result = []
    for experiment in range(number_of_experiements):
        result = []
        color_flower = False # Blue
        survived = True
        started = survive_first()
        counter = 0
        
        while not color_flower and survived and started:
            if counter == 0:
                survived = survive_first()
            else: 
                survived = survive_later() 
                
            color_flower = color_picker()
            
            print('color_flower')
            print(color_flower)
            print('survived')
            print(survived)
            
            if color_flower:
                result.append('Red')
            else:
                result.append('Blue')
            counter += 1
            
        
        all_result.append(result)
        # print(result)
    print(all_result)
    return all_result
    
def calculate(all_result):
    red_counter = 0
    blue_couter = 0
    sum_flowers = 0
    
    for result in all_result:
        for flower in result:
            sum_flowers += 1
            if flower == 'Red': 
                red_counter += 1
            else:
                blue_couter += 1
    print('red_counter')
    print(red_counter)
    print('blue_couter')
    print(blue_couter)
    print('avg_flowers')
    print(sum_flowers/len(all_result))
    print('avg red_counter')
    print(red_counter/len(all_result))
    print('avg blue_couter')
    print(blue_couter/len(all_result))
    
# 1. Ratio of red to blue
# #   2. Avg flowers per experiment
# #   3. Avg red per experiment
# #   4. Avg blue per experiment        
        
        
def color_picker():
    random_int = random.randint(1, 10) 
    color_flower = False
    if random_int % 2 == 0:
        color_flower = True
    else:
        color_flower = False
    return color_flower

def survive_first():
    random_int = random.randint(1, 20) 
    color_flower = False
    if random_int < 15: 
        color_flower = True
    else:
        color_flower = False
    return color_flower

def survive_later():
    random_int = random.randint(1, 20) 
    color_flower = False
    if random_int < 5: 
        color_flower = True
    else:
        color_flower = False
    return color_flower
    
result = simulate_experiments(7)
calculate(result)
# for i in range(5):
    # simulate_experiments(i)


# 
# Your previous Ruby content is preserved below:
# 
# def say_hello
#   puts 'Hello, World'
# end
# 
# 5.times { say_hello }
# 
# 
# 
# 
# # Write a program to generate a simulation of experiments that scientists are running. This experiment is growing flowers, red and blue. 
# 
# #    - The flowers have a 50% chance of being either red or blue.
# #    - The scientists also put a constraint on the experiment. They will plant the first flower 75% of the time.  After the first flower, they will plant each subsequent flower 25% of the time.
# #    - Once a red flower is grown, the experiment is stopped and no more flowers are planted.
# 
# # So acceptable experiments include:
# #    - Experiment 1: Blue, Blue

# #    - Experiment 2: Blue


# #    - Experiment 3: Red
# #    - Experiment 4: Blue, Red
# #    - Experiment 5:
# #    - Experiment 6: Blue, Blue, Red
# 
# # Examples of unacceptable experiments include:
# #    - Experiment 1: Red, Blue
# #    - Experiment 2: Red, Red
# #    - Experiment 3: Blue, Red, Blue
# 
# 
# # Implement a method that takes in the number of experiments to run and returns a data structure showing each experiment's flowers.
# 
# #    def simulate_experiments(2)
# #    end
# 
# # Using this method, calculate the following:
#   
# #   1. Ratio of red to blue
# #   2. Avg flowers per experiment
# #   3. Avg red per experiment
# #   4. Avg blue per experiment
