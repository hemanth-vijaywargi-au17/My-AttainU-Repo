"""
a. Print the following pattern after taking in the line number as input from the user:
for example: if input line number is 5, then print the following pattern.
  *
 ***
*****
 ***
  *
"""

n = int(input("Enter the number of lines : "))

halfway_point = ( n//2 + n%2 )

for ln in range( 1, halfway_point+1 ):
        print(" "*(n-ln),"*"*(2*ln-1))

for ln in range(halfway_point+1,n+1):
        print(" " * (ln-1), "*" *(2*(n+1-ln)-1))

# Observing the patterns we need and deriving formulas for use in our loop : ( Notes for my Understanding )
# //*     (line = 1) + (spaces = 2) = 3 (n)  --> ln + spaces = n --> spaces = n - ln (Formula made for spaces by observing pattern)
# /***    (line = 2) + (spaces = 1) = 3 (n)       [ Forumla for number of asterisk is simply 2*ln-1 as number of asterik required is
# *****   (line = 3) + (spaces = 0) = 3 (n)         always an odd number where k = nth odd number = ln]

# *****   (line_number = 1) + (spaces = 0) = 1   --> ln + spaces = (2 * ln -1) --> spaces = (2 * ln -1) - ln --> spaces = ln -1
# /***    (line_number = 2) + (spaces = 1) = 3      [  2*k-1 is the representation of all odd numbers , where k = nth odd number.
# //*     (line_number = 3) + (spaces = 2) = 5         example 2*(2)-1 = 3 (The second odd number) . In our pattern (ln + spaces) is                                                ]
#                                                           always producing odd numbers so we can say ln + spaces = (2 * ln -1),
#                                                             where k = ln ]
#          [ In reverse triangle we need to produce odd numbers in reverse order 2*(k)-1 would be the number of asterisks required in
#            our lines ,where k = nth odd number ,here k has to be number_of_lines which should keep decreasing by 1 each time the loop
#            runs.We can do this decrement by using ln , But 2*(n-ln)-1 wouldn't work for the first iteration as it would be one number
#            too short and hence we will get one line less from required number_of_lines, we can solve this by adding 1 to our formula .
#            The final result is 2*(n+1-ln)-1]

# Derived Formulas :
# 1. Triangle of n number_of_lines = 2*ln-1, where ln is line_number
# 2. Triangle Spacing = n - ln
# 3. Reverse Triangle of n number_of_lines = 2*(n+1-ln)-1
# 4. Reverse Triangle Spacing = ln -1

