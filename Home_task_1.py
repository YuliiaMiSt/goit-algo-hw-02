# Task_1

import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Лічильник для унікальних ідентифікаторів заявок
request_id = 1

# Функція для генерації нових заявок
def generate_request():
    global request_id
    new_request = f"Request {request_id}"
    request_queue.put(new_request) 
    print(f"New request generated: {new_request}")
    request_id += 1

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        current_request = request_queue.get() 
        print(f"Processing {current_request}")
        time.sleep(1)
        print(f"Completed processing {current_request}")
    else:
        print("Queue is empty. No requests to process.")

# Головний цикл програми
def main():
    while True:
        # Імітація випадкової генерації нових заявок
        if random.random() > 0.5:
            generate_request()

        process_request()

        time.sleep(2)

if __name__ == "__main__":
    main()

# Task_2

from collections import deque

def is_palindrome(s):
    # Приведемо рядок до нижнього регістру та видалимо пробіли
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Створимо двосторонню чергу з символів рядка
    d = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    return True

# Тестування функції
input_string = "A man, a plan, a canal, Panama"
print(f"'{input_string}' is palindrome: {is_palindrome(input_string)}")


# Task_3

def check_brackets(expression):
    # Створюємо стек для відкритих дужок
    stack = []
    
    # Визначаємо пари відкритих і закритих дужок
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    # Проходимо по кожному символу в рядку
    for char in expression:
        if char in '([{':  
            stack.append(char)
        elif char in ')]}': 
            if not stack or stack.pop() != bracket_pairs[char]:
                return "Несиметрично"
    
    # Якщо після проходження всієї строки в стеку є відкриті дужки, це несиметрично
    if stack:
        return "Несиметрично"
    
    return "Симетрично"

# Тестування
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",  # Симетрично
    "( 23 ( 2 - 3);",             # Несиметрично
    "( 11 }"                      # Несиметрично
]

for expr in expressions:
    print(f"{expr}: {check_brackets(expr)}")
