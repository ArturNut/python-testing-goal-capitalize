from capitalize import capitalize
""""
if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
"""
assert capitalize('hello') == 'Hello'
assert capitalize('') == ''
print('Все тесты пройдены!')
   

