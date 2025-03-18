# Create a program that, once executed the programs prints Hello  instantly first, 
# then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.
import time
i = 0
while(i<4):
    print("Hello")
    i = i+1
    time.sleep(i)
print("End of the Loop")
