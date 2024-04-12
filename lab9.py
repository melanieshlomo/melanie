def encoder(password):
    sum = ""
    for num in password:
        digit_encoder = str((int(num) + 3) % 10)
        sum += digit_encoder
    return sum


def main():
    while True:
        print("Menu")
        print("---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        option = input("Please enter an option:")
        if option == "1":
            value = input("Please enter your password to encode:")
            valuepass = encoder(value)
            print("Your password has been encoded and stored!")
            print("")
        elif option == "2":
            # userdecode = decoder(valuepass)
            # print("Decoded password is", userdecode)
            print("The encoded password is", valuepass, "and the original password is", value)
            print("")
        elif option == "3":
            break
        else:
            print("Please choose a valid option")
            print("")