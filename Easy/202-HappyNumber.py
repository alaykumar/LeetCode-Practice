class Solution:
    def isHappy(self, n: int) -> bool:

        # Convert the integer to string
        n = str(n)
        # Array to keep track of calculated square totals
        t = []

        # while loop to run until the value of 1 is reached
        while n != '1':

            # create a variable to store the total of the squared numbers total 
            s = 0

            # for loop will run iterating over each characet of the number and squaring then adding them
            for i in n:
                s += int(i) ** 2

            # Check if the calculated number is in the array, if it is return False as a loop will occur if continued
            if s in t:
                return False

            # add the calculated value into the array
            t.append(s)
  
            # convert the new squared sum number to be passed again into the for loop
            n = str(s)
        
        return True
