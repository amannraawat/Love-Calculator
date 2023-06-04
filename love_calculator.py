print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your love name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

t_count=name1_lower.count('t') + name2_lower.count('t')
r_count=name1_lower.count('r') + name2_lower.count('r')
u_count=name1_lower.count('u') + name2_lower.count('u')
e_count=name1_lower.count('e') + name2_lower.count('e')

l_count=name1_lower.count('l') + name2_lower.count('l')
o_count=name1_lower.count('o') + name2_lower.count('o')
v_count=name1_lower.count('v') + name2_lower.count('v')
e_count2=name1_lower.count('e') + name2_lower.count('e')

total_true=t_count+r_count+u_count+e_count
total_love=l_count + o_count + v_count + e_count2
total=int(f"{total_true}{total_love}")

if total < 10 or total > 90:
    print(f"\nYour score is {total}, you go together like coke and mentos.")

elif total > 40 and total < 50:
    print(f"\nYour score is {total}, you are alright together.")

else:
    print(f"\nYour score is {total}.")