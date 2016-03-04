def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return "hello world"


print convert_number(11)

print convert_number('ss')
