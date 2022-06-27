
def prime_checker(number):
    check = 0
    if number > 0:
        for n in range(2,number):
            
            if number % n == 0:
                check +=1
           
            
        if check > 0:
            print("It's not prime number")
        else:
            print("It's prime number")
      
            

n = int(input("Check this number: "))

prime_checker(number = n)