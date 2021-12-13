# -------------------------STAGE 1---------------------------------------
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
    print("\n", friends_dict, sep='')
