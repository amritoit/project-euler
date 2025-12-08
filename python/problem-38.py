def compute():
    max = 0
    # why base is in ragne 1, 10000, because more than 10000 base can not make 9 digit but more.
    for base in range(1,10000):
        concat = ''
        for i in range(1,10):
            concat += str(base*i)
            if(len(concat) == 9 and is_pandigital_1_to_9(concat)):
                print(concat)
                if(max < int(concat)):
                    max = int(concat)
            if(len(concat)>9):
                break
    return max

def is_pandigital_1_to_9(num: str):
    return sorted(num) ==  ['1','2','3','4','5','6','7','8','9']
            

print("max pandigital is:", compute())
