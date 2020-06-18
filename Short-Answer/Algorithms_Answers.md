#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The bigger 'n' is, the longer it will take for the code to finish up because of the while loop. O(n^3)

        ####### Revision
            '''
            Actually O(n), this is because it is increasing linearly, as in it is only going through one loop
            '''


b) Due to the second loop comparing values, the runtime complexity is O(n) since only the first loop is iterating.

        ###### Revision
            '''
            Since in the second loop there is a coefficient that is doubling each time the code runs, and since it till run until `j < n`, this would run in logarithmic time, O(log n).
            '''


c) This function is checking if bunnies exist, therefore the runtime complexity is O(1) since it is not iterating over anything.

        ###### Revision
            '''
            This would run in linear time, O(n), this code will run until the base case is met. As in, depending on the size of the input, the longer or less time it will take until it reaches 0.
            '''

## Exercise II
    The algorithm would need to find the last floor in which the end doesn't break and the first floor in which it does. O(log n)

