# -------------------------STAGE 1---------------------------------------
# friends_dict = {}
#
# print("Enter the number of friends joining (including you):")
# count = int(input())
# print()
# if count < 1:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     for i in range(count):
#         friends_dict[input()] = 0
#     print("\n", friends_dict, sep='')

# -------------------------STAGE 2---------------------------------------
friends_dict = {}

print("Enter the number of friends joining (including you):")
count = int(input())
print()
if count < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(count):
        friends_dict[input()] = 0
    print("Enter the total bill value:")
    try:
        total = int(input())
        per_person = round(total / count, 2)
    except ValueError:
        print("Non-correct total bill value!")
    else:
        for friend in friends_dict.keys():
            friends_dict[friend] = per_person
    finally:
        print("\n", friends_dict, sep='')
