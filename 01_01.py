def ordered_insert(list, n):
 
    index = len(list)
    # Searching for the position
    for i in range(len(list)):
      if list[i] > n:
        index = i
        break
 
    # Inserting n in the list
    if index == len(list):
      list = list[:index] + [n]
    else:
      list = list[:index] + [n] + list[index:]
    return list


with open('01_01_input.txt', 'r') as file:
    column1 = list()
    column2 = list()
    for line in file:
        num1, num2 = line.strip().split('   ')
        column1 = ordered_insert(column1, int(num1))
        column2 = ordered_insert(column2, int(num2))
    
    # add up all of the distances
    total_distance = sum([abs(a-b) for a,b in zip(column1,column2)])
    print(total_distance)

    # add up similarity score

    i = 0
    j = 0
    similarity_counts = [0]*len(column1)
    similarity_sum = 0
    while i in range(len(column1)) and j in range(len(column2)):
        if column1[i] > column2[j]: 
          j +=1
        else:
          while column1[i] == column2[j]:
              similarity_counts[i] += 1
              j +=1
          similarity_sum += column1[i] * similarity_counts[i]
          i+=1
    print(similarity_sum)
    

  
