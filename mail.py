#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program tells user the month afte typing the number


def mailing(name, last_name, st_address, city, province, postal_code,
            apt_number=None):
    # This function organizes the mailing address to standardized

    name_address = name + " " + last_name
    name_address = name_address
    if apt_number != None:
        address = apt_number + " - " + st_address
    else:
        address = st_address
    address2 = city + " " + province + "  " + postal_code

    mailing_address = name_address.upper() + "\n" + address.upper() + "\n" + address2.upper()

    return mailing_address


def main():
    # This function gets input from user and calls other functions
    apt_number = None

    name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("")
    question = input("Do you have an apartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter the apartment number : ")
    st_address = input("Enter the street address: ")
    city = input("Enter the city: ")
    province = input("Enter The province: ")
    postal_code = input("Enter the postal code: ")
    print("")

    if apt_number != None:
        address = mailing(name, last_name, st_address, city, province,
                          postal_code, apt_number)
    else:
        address = mailing(name, last_name, st_address, city, province,
                          postal_code)
    print(address)


if __name__ == "__main__":
    main()
