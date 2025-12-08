def is_palindrom(num):
    num_str = str(num)
    reversed_num = num_str[::-1]
    if num_str == reversed_num:
        return True
    return False

def compute():
    total_sum = 0
    for i in range(1000000):
        if(is_palindrom(i) and is_palindrom(format(i, 'b'))):
            print(format(i, 'b'))
            total_sum += i
    print(total_sum)

compute()
