import logging

logging.basicConfig(filename="NewLog.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
#result = 0


def DoCalc(num1, num2):
    if num1 < 0 or num2 < 0:
        print("No negative numbers")
        logging.debug("Error")
        logging.error("You entered negative number")
        logging.info("Number can not be negative")
    else:
        result = num1 + num2
        logging.info("Addition Successful")
        print(result)


DoCalc(num1, num2)

# try:
#    numerator = 10
#   denominator = 0
#
#   result = numerator/denominator
#
#   print(result)
# ex#cept:
# print("Error: Denominator cannot be 0.")
