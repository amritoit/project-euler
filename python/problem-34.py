class Compute:
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]  # Precompute factorials of digits 0-9
    def run(self):
        total_sum = 0
        for i in range(3, 2540161):
            if i == sum(self.factorials[int(d)] for d in str(i)):
                print(i)
                total_sum += i

        print("Total sum:", total_sum)

Compute().run() # Call the run method to execute the computation
# The upper limit 2540161 is chosen because 9! * 7 = 2540160, which is the maximum sum of factorials for a 7-digit number.
# This code finds and prints all numbers that are equal to the sum of the factorials of