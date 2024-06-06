# temp of a city in fahrenheit degree is input through keyboard.write a program to convert this tempreture into centigrade degree
f =float (input("enter tempreture of city in fahrenheit degree :"))
c =  float( f - 32) * 5/9
print("fahrenheit degree =",f)
print("celsius degree =",c)

# Checked correct 5/5
# just a better way to write print statement using concept known as f string
# just write f ahead of " like print(f" then write the content and if want to use any variable write its name in {variable_name} and complete print")
print(f"fahrenheit degree = {f}")
print(f"celsius degree = {c}")
