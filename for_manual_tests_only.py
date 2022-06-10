from string import ascii_lowercase
import random
def creating_name_from_numbers_and_lowercase():
    numbers='0123456789'
    symbol='-'
    all =  ascii_lowercase + numbers
    lenght_1 = 8
    lenght_2 = 4
    lenght_3 = 12
    mid_lenght_part ="".join(random.sample(all, lenght_1))
    short_lenght_part = "".join(random.sample(all, lenght_2))
    long_lenght_part = "".join(random.sample(all, lenght_3))
    name =mid_lenght_part+symbol+(short_lenght_part+symbol)*3+long_lenght_part
    return name

creating_name_from_numbers_and_lowercase()