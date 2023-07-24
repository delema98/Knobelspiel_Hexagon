import time
import itertools

tstart = time.time()

outputFile = "results_permutations.txt"
max_value = 20
sum_of_each_row = 38
allSolutions = []

# Generate all possible permutations of max_value length 
for p in itertools.permutations(range(1, max_value+1), 19):

    # all conditions
    if (sum(p[0:3]) == sum_of_each_row 
        and sum(p[3:7]) == sum_of_each_row             
        and sum(p[7:12]) == sum_of_each_row             
        and sum(p[12:16]) == sum_of_each_row                 
        and sum(p[16:19]) == sum_of_each_row 
        and p[0]+p[4]+p[9]+p[14]+p[18] == sum_of_each_row 
        and p[2]+p[6]+p[11]+p[15] == sum_of_each_row 
        and p[7]+p[8]+p[9]+p[10]+p[11] == sum_of_each_row 
        and p[1]+p[5]+p[10]+p[15] == sum_of_each_row 
        and p[0]+p[3]+p[7] == sum_of_each_row 
        and p[12]+p[13]+p[14]+p[15] == sum_of_each_row 
        and p[16]+p[17]+p[18] == sum_of_each_row 
        and p[2]+p[6]+p[11] == sum_of_each_row 
        and p[3]+p[8]+p[13]+p[17] == sum_of_each_row 
        and p[6]+p[10]+p[14]+p[17] == sum_of_each_row):

        allSolutions.append(p)

# Write all solutions to the file at once
with open(outputFile, "w") as daten:
    for solution in allSolutions:
        daten.write("\n{}".format(solution))

execution_time = time.time() - tstart

print("Program finished")
print("all Solutions: {}".format(len(allSolutions)))
print("execution time: {}".format(execution_time))
