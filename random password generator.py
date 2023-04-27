import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()";
password_length=int(input("enter your password length: "));
a="".join(random.sample(password,password_length));
print(f"your random password is:  {a}");
