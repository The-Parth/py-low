"""
Armstrong number checker.
"""
def main():
    no = int(input("Enter a number: "))
            
    if armstrongCheck(no):
        print(no, "is an Armstrong number.")
    else:
        print(no, "is not an Armstrong number.")
        
        
def armstrongCheck(no: int) -> bool:
    x = no
    sm = 0
    while x != 0:
        sm += (x % 10) ** 3
        x //= 10
    if sm == no:
        return True
    else :
        return False
    

if __name__ == "__main__":
    main()