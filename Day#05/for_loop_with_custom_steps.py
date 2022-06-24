#a to b but not included b
# for number in range(a,b): default increase number by 1
# for number in range(a,b,number_of_step): custom increase number 
#for number in range(a,b):
	#print(number)

# Will print number from 1 to 20(inclued)
for number in range(1,21):
    print(number)
    
#custom step
print("################################################") 
for number in range(1,21,3):
    print(number)
    
    
print("----------------------")

total = 0

for number in range(1, 101):
    total += number

print(total)