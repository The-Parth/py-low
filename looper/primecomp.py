def main():
    prime = composite = 0
    while True:
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("That's not a number!")
            continue
        if n == -1:
            print("Number entered is -1. Exiting...")
            print("Number of prime numbers entered:", prime)
            print("Number of composite numbers entered:", composite)
            break
        
        res = primeComp(n)
        if res == True:
            prime += 1
        elif res == False:
            composite += 1
        
def primeComp(n: int) -> bool:
    if n == 1 or n == 0:
        return None
    if n < 0:
        print("Number entered is negative. Invalid!")
        return None
    if factorCount(n) == 1:
        return True
    else:
        return False
    

def factorCount(n: int) -> int:
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count

if __name__ == "__main__":
    main()