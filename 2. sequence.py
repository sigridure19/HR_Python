#Design an algorithm that generates 
#the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Talnaröðin byggist á að 3 tölurnar á undan eru lagðar 
# saman og gildið úr því verður næsta tala í rununni

#n(x) = n(x-1)+n(x-2)+n(x-3)

n = int(input("Enter the length of the sequence: ")) # Do not change this line

# n(counter) = n(counter-1) + n(counter-2) + n(counter -3)
sequence_int = 0
counter = 0

for i in range(1,n + 1):
    counter +=1
    if i == 1:
        sequence_int = n_1 = counter 
    elif i == 2:
        sequence_int = n_2 =  counter
    elif i == 3:
        sequence_int = n_3 =counter 

# n_1 , n_2 , n_3 eru liðirnir þrír sem þarf að leggja saman til þess að fá röðina
        
    else:
        sequence_int = n_1 + n_2 + n_3
        n_1, n_2, n_3 = n_2, n_3, sequence_int # endurskilgreini liðina þannig að fyrsti liðurinn dettur
        # og næsti liður í rununni bætist við.
    print(sequence_int, end =" ")





    
