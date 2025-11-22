# Finding out new types of mathematical operations that weren't in Javascript

my_int = 3
my_float = 1.15

adding_float = float(my_int)
removing_float = int(my_float)

my_div = my_int / my_float
my_floor = my_int // my_float
my_exp = my_int ** my_float

my_round = f"{my_float} > {round(my_float)}"
my_bin = f"{my_int} > {bin(my_int)}"
my_oct = f"{my_int} > {oct(my_int)}"
my_hex = f"{my_int} > {hex(my_int)}"

full_text = f"""
INTEGER {my_int} / FLOAT {my_float}
INTEGER TURNED FLOAT {adding_float} / FLOAT TURNED INTEGER {removing_float}

regular division: {my_div}
floor division: {my_floor}
exponent: {my_exp}

round: {my_round}
binary: {my_bin}
octal: {my_oct}
hexadecimal: {my_hex}

"""
print(full_text)