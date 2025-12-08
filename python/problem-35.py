class Compute:
    primes=[]
    def sieve(self):
        is_prime=[True]*1000000
        is_prime[0]=is_prime[1]=False
        for i in range(2,1000000):
            if is_prime[i]:
                self.primes.append(i)
                for j in range(i*i,1000000,i):
                    is_prime[j]=False

    def run(self):
        self.sieve()
        prime_set=set(self.primes)
        circular_primes=[]
        for prime in self.primes:
            s=str(prime)
            length=len(s)
            is_circular=True
            for i in range(length):
                rotated=int(s[i:]+s[:i])
                if rotated not in prime_set:
                    is_circular=False
                    break
            if is_circular:
                circular_primes.append(prime)
        return len(circular_primes)
    
number_of_cp = Compute().run()
print(number_of_cp)