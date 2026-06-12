# def my_function():
#     result = 2 * 3
#     return result
#
# output = my_function()

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("bunkuiyi", "olagunju")

print(formatted_string)

# Why return instead of print

def function_1(text):
    return text + text


def function_2(text):
    return text.title()

output = function_2(function_1("hello world"))
print(output)