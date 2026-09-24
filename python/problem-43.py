# problem-43.py ---
# Filename: problem-43.py
# Description: https://projecteuler.net/problem=43
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Mon Jul 22 18:53:27 2019 (+0530)
# Last-Updated:
#           By:
#     Update #: 22
#
# Set to True to print step-by-step diagnostics while solving.
DEBUG = False


class SubStringDivisibility:
    """
    Finds all 0-9 pandigital numbers whose substrings d2d3d4, d3d4d5, ...,
    d7d8d9 (each 3 digits long) are divisible by 2, 3, 5, 7, 11, 13 and 17
    respectively, and sums them (Project Euler problem 43).

    Approach: build a 10-digit pandigital number "from right to left" by
    picking 3-digit blocks that overlap by 2 digits with the previously
    chosen block, and that are divisible by the divisor associated with
    that position. A bitmask tracks which digits have already been used
    so the final number stays pandigital (each digit 0-9 used exactly once).
    """

    def __init__(self):
        # Maps each divisor -> list of 3-digit numbers (with distinct digits)
        # that are divisible by that divisor. Populated by compute().
        self.store = {}
        # divisor[i] is the divisor that the i-th 3-digit substring (from
        # the right) must be divisible by. divisor[0] = 1 is a sentinel
        # used for the right-most block (d1d2d3), which has no divisibility
        # requirement of its own.
        self.divisor = [1, 2, 3, 5, 7, 11, 13, 17]

    def compute(self):
        """Pre-compute, for every divisor, all 3-digit numbers (000-999)
        with 3 distinct digits that are divisible by that divisor."""
        for num in range(10, 1000):
            str_num = str(num).zfill(3)
            if len(set(str_num)) != 3:
                continue  # skip numbers with repeated digits
            for c in self.divisor:
                if num % c == 0:
                    self.store.setdefault(c, []).append(num)

    def countSubStringsDivisibility(self, divisorIndex, mask, numSoFar):
        """
        Recursively extends the number being built by one digit to the left,
        trying every candidate 3-digit block for the current divisor.

        divisorIndex: index into self.divisor for the block currently being
                      chosen; recursion proceeds from the last divisor (17)
                      down to the sentinel (1).
        mask: bitmask of digits already used elsewhere in the number.
        numSoFar: the digits chosen so far, as a string, built up from the
                  right-most block outwards (so its first character is the
                  most recently added, left-most digit so far).

        Returns the sum of all valid full pandigital numbers found in this
        branch of the search.
        """
        result = 0
        if DEBUG:
            print("divisorIndex", divisorIndex, numSoFar)

        for num in self.store[self.divisor[divisorIndex]]:
            num = str(num).zfill(3)
            newmask = mask

            if numSoFar != "":
                # The new block must overlap the previous block's first two
                # digits (i.e. its last two digits must match numSoFar[0:2]).
                prevDigits = numSoFar[0:2]
                if DEBUG:
                    print("prevDigits=", prevDigits, ",num=", num, ",num[1:3]=", num[1:3])
                if prevDigits != num[1:3]:
                    continue

            # The new digit being introduced is num[0]; it must not have
            # been used already elsewhere in the number.
            if newmask & (1 << int(num[0])):  # digit already used -> reject
                continue
            newmask |= (1 << int(num[0]))

            if divisorIndex > 0:
                if numSoFar == "":
                    # First block placed: also reserve its other two digits.
                    newNumSoFar = num
                    newmask |= (1 << int(num[1]))
                    newmask |= (1 << int(num[2]))
                else:
                    # Only the new left-most digit needs to be prepended,
                    # since the other two digits overlap with numSoFar.
                    newNumSoFar = num[0] + numSoFar
                result += self.countSubStringsDivisibility(divisorIndex - 1, newmask, newNumSoFar)
            else:
                # divisorIndex == 0 is the sentinel divisor (1): the number
                # is now complete (all 10 digits chosen).
                newNumSoFar = num[0] + numSoFar
                if DEBUG:
                    print("numSoFar=", newNumSoFar)
                result += int(newNumSoFar)

        if DEBUG:
            print("result", result)
        return result

    def solve(self):
        self.compute()
        return self.countSubStringsDivisibility(len(self.divisor) - 1, 0, "")


if __name__ == "__main__":
    solver = SubStringDivisibility()
    print("Answer", solver.solve())