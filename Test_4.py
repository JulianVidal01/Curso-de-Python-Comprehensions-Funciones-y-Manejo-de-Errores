def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda x: x * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)