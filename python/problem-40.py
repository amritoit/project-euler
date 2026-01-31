def find_nth_digit_number(n):
    """
    Find the nth digit in the sequence of all natural numbers concatenated together.
    e.g., 123456789101112... from this, I need to find the nth digit number. if n=10, the answer is 10
    
    :param n: The position of the digit to find
    :return: The nth digit as an integer
    """
    
    bucket = 1
    total_num_of_digits_so_far = 0
    cache_of_total_digit_count_by_bucket = {}
    while True:
        if n <= 9:
            break
        else:
            total_num_of_digits_so_far += bucket * 9 * 10**(bucket - 1)
            cache_of_total_digit_count_by_bucket[bucket] = total_num_of_digits_so_far 
            if n <= total_num_of_digits_so_far:
                break
        bucket += 1
    # We found the bucket where the nth digit is located
    # bucket 1: 1-9 (9 digits)
    # bucket 2: 10-99 (90 numbers, 180 digits)
    # bucket 3: 100-999 (900 numbers, 2700 digits)

    previous_total = cache_of_total_digit_count_by_bucket.get(bucket - 1, 0)
    offset_in_bucket = n - previous_total - 1  # zero-based index
    bucket_size = 10**(bucket - 1)
    number_index = offset_in_bucket // bucket
    digit_index = offset_in_bucket % bucket
    number = bucket_size + number_index
    nth_digit = str(number)[digit_index]
    return int(nth_digit)

result = find_nth_digit_number(1) * find_nth_digit_number(10) * find_nth_digit_number(100) * find_nth_digit_number(1000) * find_nth_digit_number(10000) * find_nth_digit_number(100000) * find_nth_digit_number(1000000)
print("The result is:", result)
assert find_nth_digit_number(12) == 1
assert find_nth_digit_number(11) == 0
assert find_nth_digit_number(10) == 1
assert find_nth_digit_number(9) == 9
assert find_nth_digit_number(190) == 1
assert find_nth_digit_number(189) == 9