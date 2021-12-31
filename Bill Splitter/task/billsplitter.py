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

# # -------------------------STAGE 2---------------------------------------
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
#     print("Enter the total bill value:")
#     try:
#         total = int(input())
#         per_person = round(total / count, 2)
#     except ValueError:
#         print("Non-correct total bill value!")
#     else:
#         for friend in friends_dict.keys():
#             friends_dict[friend] = per_person
#     finally:
#         print("\n", friends_dict, sep='')

# # -------------------------STAGE 3---------------------------------------
# import random
#
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
#     print("Enter the total bill value:")
#     try:
#         total = int(input())
#         print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
#         answer = input()
#         if answer == 'Yes':
#             lucky = random.choice(list(friends_dict.keys()))
#             print(f"{lucky} is the lucky one!")
#         else:
#             print("No one is going to be lucky")
#             # per_person = round(total / count, 2)
#     except ValueError:
#         print("Non-correct total bill value!")
#     # else:
#     #     for friend in friends_dict.keys():
#     #         friends_dict[friend] = per_person
#     # finally:
#     #     print("\n", friends_dict, sep='')

# -------------------------STAGE 4---------------------------------------
import random

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
    except ValueError:
        print("Non-correct total bill value!")
    else:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer == 'Yes':
            lucky = random.choice(list(friends_dict.keys()))
            print(f"{lucky} is the lucky one!")
            per_person = round(total / (count - 1), 2)
            for friend in friends_dict.keys():
                if friend == lucky:
                    friends_dict[friend] = 0
                else:
                    friends_dict[friend] = per_person
        else:
            print("No one is going to be lucky")
            per_person = round(total / count, 2)
            for friend in friends_dict.keys():
                friends_dict[friend] = per_person
    finally:
        print("\n", friends_dict, sep='')