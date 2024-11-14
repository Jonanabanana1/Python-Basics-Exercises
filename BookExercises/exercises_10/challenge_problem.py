# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
# Outer loop is each list inside of my_list
# Inner loop is each element inside of each list
# Check if element % 2 == 0, if so print the element
outerIndex = 0
while outerIndex < len(my_list): 
    innerIndex = 0
    while innerIndex < len(my_list[outerIndex]):
        if my_list[outerIndex][innerIndex] % 2 == 0:
            print(my_list[outerIndex][innerIndex])
        innerIndex+=1
    outerIndex+=1
