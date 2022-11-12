# TODO решить с помощью list comprehension и распечатать ег


from pprint import pprint
# pprint({1:{val for val in enumerate(range(10))},
#        3:list(range(15)),
#        4:2}
#         )
a = [{'bin': bin(val), 'dec': val, 'hex': hex(val), 'oct': oct(val)} for val in range(16)]
pprint(a)

