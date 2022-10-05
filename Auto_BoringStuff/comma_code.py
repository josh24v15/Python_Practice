"""Write a function that takes a list value as an argument and returns a string 
with all the items separated by a comma and a space, with and inserted before the last item."""

def andFunction(inputs):
    if not inputs:
        print("There are no input values.")
        return None
    else:
        values = ', '.join(str(inputs[i]) for i in range(len(inputs) - 1))
        values += ', and ' + str(inputs[len(inputs) - 1])
        print(values)    

andFunction(['Hi', 'how', 'are', 'you', '?'])
andFunction([2, 3, 4, 5])
andFunction('')