# PART 2: Pushing sys.argv to the limit

import sys #1
def main (): #2
   if len(sys.argv) !=4: #3
       print("Usage: python script.py <arg1> <arg1> <arg2> <arg3>") #4
       sys.exit(1) #5
   result = sum(map(int, sys.argv[1:]))  #6
   print("Result:", "w") as file: #7
   with open("output.text", "w") as file: #8
       file.write(str(result)) #9
       print("Result written to 'output.text'.") #10
if __name__ == "__main__": #11
    main() #12