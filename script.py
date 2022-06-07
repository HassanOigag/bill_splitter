import random

def calculate_shares(amount, number_of_people):
    share = round(amount / number_of_people, 2)
    if share.is_integer():
        share = int(share)
    return share

def get_number_of_people():
    try:
        number_of_people = int(input("Enter the number of friends joining (including you):\n"))
        assert number_of_people > 0
    except (ValueError, AssertionError):
        print("\nNo one is joining for the party")
        exit()
    else:
        return number_of_people

def get_names(number_of_people):
    names = []
    print("\nEnter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_people):
        name = input()
        if name:
            names.append(name)
    return names

def get_bill_total():
    try:
        bill = float(input("\nEnter the total bill value:\n"))
        assert bill >= 0
    except (ValueError, AssertionError):
        print("should be a positive number")
        exit()
    else:
        return bill

if __name__ == "__main__":
    people = {}
    number_of_people = get_number_of_people()
    for name in get_names(number_of_people):
        people[name] = 0
    bill = get_bill_total()
    answer = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    lucky_friend = ""
    if answer == "yes":
        lucky_friend = random.choice(list(people.keys()))
        print(f"\n{lucky_friend} is the lucky one!")
        share = calculate_shares(bill, number_of_people - 1)
    else:
        print("\nNo one is going to be lucky") 
        share = calculate_shares(bill, number_of_people) 

    for name in people.keys():
        if name != lucky_friend:
            people[name] = share

    print()
    print(people)