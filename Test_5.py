def filter_by_length(words):
    result = list(filter(lambda x : len(x) >= 4, words))
    return result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)