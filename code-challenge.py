#Add up and print the sum of the all of the minimum elements of each inner array:
sample_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

def sum_of_minimum_element(arr):
    #set count variable equal to zero
    count = 0
    #loop through my array of arrays
    for item in arr:
        #find the minimum in each arr
        minimum = min(item)
        #add that minimum to the count variable
        count += minimum
    #return the count variable
    return count

print(sum_of_minimum_element(sample_arr))