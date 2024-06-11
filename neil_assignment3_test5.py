#write a program to input marks of five subjects and calculate percentage calculate grade also percentage>=90%A percentage>=80%b percentage>=70%c percentage>=60%d  percentage>=40%e percentage<40%fail
sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100
if percentage >= 90:
 print("grade= A")
elif percentage >= 80:
 print("grade= B")
elif percentage >= 70:
 print("grade= C")
elif percentage >= 60:
 print("grade= D")
elif percentage >= 40:
 print("grade= E")
else:
   print("fail")
print("Total marks=", total_marks)
print("Percentage=", percentage)