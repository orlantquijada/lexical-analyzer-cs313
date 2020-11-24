from project import is_assignment_valid

print("check if an assignment statement is valid or not:")
print("valid" if is_assignment_valid(input()) else "invalid")


print("\n\nsample tests:")
# valid assignments
print("valid" if is_assignment_valid("num1 = num2;") else "invalid")
print("valid" if is_assignment_valid("num1 = 10;") else "invalid")
print("valid" if is_assignment_valid("num1 = 10.50;") else "invalid")
print("valid" if is_assignment_valid("num1 = 'a';") else "invalid")
print("valid" if is_assignment_valid('num1 = "a";') else "invalid")
print("valid" if is_assignment_valid("_1_a=1+2/num1 *asdf% qwerty;") else "invalid")
print("valid" if is_assignment_valid("___ = 1;") else "invalid")
print("valid" if is_assignment_valid("asd_123 = 1;") else "invalid")
print("valid" if is_assignment_valid("__1__asd123 = 1;") else "invalid")
print("valid" if is_assignment_valid("num1 =1+ num2+ 'a';") else "invalid")
print("valid" if is_assignment_valid("____1asdd = 12. + '='       ;  ") else "invalid")
print("valid" if is_assignment_valid("a_1_f_2 = ';'/ 2.0 + .1 + 2.;") else "invalid")
print("valid" if is_assignment_valid("num =  \";\" + 'a' % num2;") else "invalid")

print("\n")
# invalid assignments
print("valid" if is_assignment_valid("num1 = + 10.50 + num2;") else "invalid")
print("valid" if is_assignment_valid("num2 = 10.50 + num1 * 10 /;") else "invalid")
print("valid" if is_assignment_valid("num2 = 10.50+num1*+10/18.5;") else "invalid")
print("valid" if is_assignment_valid("num1=;") else "invalid")
print("valid" if is_assignment_valid("num1=") else "invalid")
print("valid" if is_assignment_valid("num1 = 1   ") else "invalid")
print("valid" if is_assignment_valid("num1 = + 10 + ;") else "invalid")