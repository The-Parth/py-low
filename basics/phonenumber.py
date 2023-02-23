def function():
    print("Phone number checker! ")
    ch = False
    no = input("Enter phone number: ")
    no = no.strip()
    if no.isdigit():
        if len(no) == 10:
            ch = True

    if ch:
        print("Is valid phone number")
    else:
        print("Not a valid phone number")

if __name__ == "__main__":
    function()
