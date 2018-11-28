import random

list_num = ["1", "2", " ", "3", "4", " ", "5", "6", "7", " ", "8", "9", "0"]
list_alpha = ["a", "b", "c", "d", " ", "e", "f", "g", " ", "h", "i", "k", " " "l", "m", "n", "o", "p", "q", "r", " ", "s", "t", "u", "v", "w", "x", "y", "z"]
list_symb = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+", "?" ">", "<", ".", ",", ":", ";"]
list_mix = list_num + list_alpha
list_mix_hard = list_mix + list_symb

pass_length = random.randint(8, 13)
ran_num = random.randint(1, len(list_num))
ran_symb = random.randint(1, len(list_symb))

strong = input("How strong your password want to be? 1 = week 2, = medium, 3 = strong: ")

new_password = ""
print("Password length is:", pass_length)

if int(strong) == 1:
    while len(new_password) <= pass_length:
        ran_lu = random.randint(1, 2)
        if ran_lu == 1:
            ran_alpha = random.randint(1, len(list_alpha)-1)
            new_password += list_alpha[ran_alpha]
        else:
            ran_alpha = random.randint(1, len(list_alpha) - 1)
            new_password += list_alpha[ran_alpha].upper()

elif int(strong) == 2:
    while len(new_password) <= pass_length:
        ran_mix = random.randint(1, len(list_mix)-1)
        new = list_mix[ran_mix]
        if new.isdigit():
            new_password += new
        elif new.isalpha():
            ran_lu = random.randint(1, 2)
            if ran_lu == 1:
                new_password += new
            else:
                new_password += new.upper()
        else:
            new_password += new
elif int(strong) == 3:
    while len(new_password) <= pass_length:
        ran_mix = random.randint(1, len(list_mix_hard)-1)
        new = list_mix_hard[ran_mix]
        if new.isdigit():
            new_password += new
        elif new.isalpha():
            ran_lu = random.randint(1, 2)
            if ran_lu == 1:
                new_password += new
            else:
                new_password += new.upper()
        else:
            new_password += new

print("The password is:\n", new_password)