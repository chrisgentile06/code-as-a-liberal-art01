from unit1lesson2 import *
number_list.sort ()
print ("smallest element is:", number_list[0])
#smallest number is 175, the sorting function sorts the numbers from lowest to hights, then you start at 0 for the first number
print("No of elements in list are:", len(number_list))

def closest(number_list, K):
    return number_list[min(range(len(number_list)), key = lambda i: abs(number_list[i]-K))]
K=500
print("The closest number to 500 is:", closest (number_list, K))
#closest number to 500 is 499
number_list.sort()

for x in number_list:
    if x > 500:
        print(x) # answer is 501
        break
#this gives you the closest number ABOVE 500

even_numbers = []
for num in number_list:
    if num % 2 == 0:
        even_numbers.append(num)
        even_numbers.sort()
print(even_numbers[0])
#smallest even number is 176

#define a function
def sortSmallToBig(number_list):
    smallest = number_list[0]
    if number_list[1] < smallest:
        smallest = number_list[1]
    for x in number_list:
        if x < smallest:
            smallest = x
        return smallest



word_list.sort (reverse= True)
print ("the last word alphabetically is:", word_list[0])
#last word is violation

word = max(word_list, key = len)
print("Longest word is:" + word)
#longest word is rehabilitation 