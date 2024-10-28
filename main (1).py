
#Basic(1-10)

#1 Hello World
print("Hello World")

#2 Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")

#3 Check if a Number is Prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#4Fibonacci Sequence

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence
#5 Factorial Calculation

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# Factorial Calculation

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


#6 Find Maximum of a List

def find_max(numbers):
    return max(numbers)


#7 Reverse a String

def reverse_string(s):
    return s[::-1]


#8 Find Average of a List


def find_average(numbers):
    return sum(numbers) / len(numbers)


#9 Check Palindrome


def is_palindrome(s):
    return s == s[::-1]



#10 Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
# Intermediate Label Python program

#11 Sorting a List 

def sort_list(numbers):
    return sorted(numbers)


#12 Count World Frequency in try:
    


 from collections import Counter
def word_frequency(text):
    words = text.split()
    return Counter(words)


#13 Binary Search

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#14 Remove Duplicates from a List

def remove_duplicates(lst):
    return list(set(lst))



#15 Find Second Largest Number

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]


#16 List Comprehension


squares = [x**2 for x in range(1, 11)]


#17 Count Vowels in a String


def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')



#18Lambda Function for Squaring

square = lambda x: x**2


#19 Map and Filter Example


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))


#20 Calculate GCD

import math
gcd = math.gcd(24, 36)

#21 Simple File Read and Write


with open('file.txt', 'w') as f:
    f.write('Hello, World!')
with open('file.txt', 'r') as f:
    print(f.read())


#22 Bubble Sort Algorithm



def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#23 Merge Two Sorted Lists


def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)


#24 Convert JSON to Dictionary


import json
json_data = '{"name": "Arif", "age": 23}'
data = json.loads(json_data)



#25 Exception Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



#Advanced (26-40)


#26 Implementing a Class and Object


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
arif = Person("Arif", 23)


#27 Binary Tree Implementation


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#28 Linear Regression with NumPy


import numpy as np
X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 1.3, 3.75, 2.25])
m, c = np.polyfit(X, y, 1)


#29 Decorator Function


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


#30 DataFrame Manipulation with Pandas



import pandas as pd
data = {'Name': ['Arif', 'Mia'], 'Age': [23, 25]}
df = pd.DataFrame(data)



#31 Finding Correlations in a Dataset



import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
correlations = df.corr()



#32 Using Matplotlib for Data Visualization


import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()



#33 Random Forest with Scikit-Learn


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)


#34 Regular Expressions


import re
text = "The rain in Spain"
match = re.search("rain", text)


#35 Working with Dates


from datetime import datetime
now = datetime.now()


#36 Web Scraping with BeautifulSoup

from bs4 import BeautifulSoup
import requests
page = requests.get("http://example.com")
soup = BeautifulSoup(page.content, "html.parser")


#37 Calculate ROC and AUC


from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)


#38 Natural Language Processing


from nltk.tokenize import word_tokenize
sentence = "Natural language processing is fun!"
words = word_tokenize(sentence)


#39 Building a Neural Network with Keras


from keras.models import Sequential
from keras.layers import Dense
model = Sequential([Dense(32, activation='relu'), Dense(1, activation='sigmoid')])



#40 Creating a Simple REST API with Flask


from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})






