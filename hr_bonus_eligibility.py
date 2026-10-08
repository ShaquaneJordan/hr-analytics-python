# declaring variables, "tenure" and "rating" as user input
# formatted as integer
tenure = int(input("Years with company: "))
rating = int(input("Performance rating (1-5): "))

# if tenure is greater than or equal to 2 AND rating is greater than or equal to 3
# then print "Eligible for bonus" and if not then print "Not eligible for bonus"
if tenure >= 2 and rating >= 3:
    print("Eligible for bonus")
else:
    print("Not eligible for bonus")
