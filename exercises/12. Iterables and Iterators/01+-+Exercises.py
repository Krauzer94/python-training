#### Question 1

# Given the following list:
l = [10, 'abc', 3.14, True]

# Print index and value for each element
for i, val in enumerate(l):
    print(f'(#{i}) - {val}')

#### Question 2

# Create a generator expression that produces numbers raised to their own power
gen_exp = (i ** i for i in range(1, 10_001))

# Timing the generator expression
from time import perf_counter

start = perf_counter()
for _ in range(10):
    gen_exp = (i ** i for i in range(1, 10_001))
    for _ in range(5):
        print(next(gen_exp))
end = perf_counter()
print('\nGenerator elapsed:', end - start)

# Timing the list comprehension
start = perf_counter()
result = [i ** i for i in range(1, 10_001)]
for _ in range(10):
    for val in result[:5]:
        print(val)
end = perf_counter()
print('\nList comprehension elapsed:', end - start)
