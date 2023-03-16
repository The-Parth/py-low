def main():
    while True:
        try:
            ls = list(map(float,input("Enter a space-seprated list of numbers: ").split()))
            break
        except ValueError:
            print("Error: Enter only numbers separated by space")

    ls.sort()
    print("Sorted list: ",ls)

    while True:
        try:
            no = int(input("Enter a number to search:"))
            break
        except ValueError:
            print("Invalid number!")
    
    res = binary_search(ls,no)
    if (res != -1):
        print("Number found at index",res)
    else:
        print("Number not found!")
        
def binary_search(ls,no):
    low = 0
    high = len(ls)-1
    while low <= high:
        mid = (low+high)//2
        if no == ls[mid]:
            return mid
        elif no < ls[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

if __name__ == "__main__":
    main()