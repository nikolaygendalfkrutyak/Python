import os
def greetings_decorator(func):
    file = open('data_log.txt', 'a')
    def wrapper(*args, **kwargs):
        res = f'Hello, {func(*args, **kwargs)}!'
        file.writelines(f"{res} \n")
        file.close()
        return res
    return wrapper

@greetings_decorator
def transform_name(first_name, last_name):
    return f'{last_name.upper().strip()} {first_name.upper().strip()[0]}.'


@greetings_decorator
def transform_name_title(full_name):
    return f'{full_name.title().strip()}'


print(transform_name('John', 'Doe'))
print(transform_name_title('john doe'))
