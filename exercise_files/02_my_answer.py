def factorial(num):
    # use isinstance() function to check type of a variable
    # it's better to use isinstance() than type() because it blocks flexibility of polymorphism
    # source: https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
    # difference between isinstance() and type(): https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
    # isintance() includes subclasses, while type() does NOT include subclasses
    output = 1
    if isinstance(num, int) and (num >= 0):
        for counter in range(0,num):
            output = output * (counter + 1)
        return output
    else:
        return print(output)

# alternative answer:
# def factorial(num):
#     output = num
#     if num == 0:
#         return 1
#     if isinstance(num, int) and (num > 0):
#         num = output - 1
#         while num > 0:
#             output = output * num
#             num = num - 1
#         return output
#     else:
#         return print(output)

number = 5
result = factorial(number)
print(result)
