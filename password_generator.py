import random
print("PASSWORD GENERATOR")
n = int(input("Enter the length of the password: "))
password = ""
for i in range(n):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
print(f"Generated password: {password}")