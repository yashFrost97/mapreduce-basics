import sys
count = 0

data1 = []
data2 = []
for line in sys.stdin:

	line = line.strip()

	val = line.split("\t")

	if len(val) == 2:
		data1.append(val)
	else:
		data2.append(val)

for i in data1:
	emp_id = i[0]
	name = i[1]
	for j in data2:
		if(j[0] == emp_id):
			print(emp_id, ' ', name, ' ', j[1], ' ', j[2], ' ', j[3])

	



# for i in range(int(len(data)/2)):

# 	print(i)

# 	emp_id = data[i][0]
# 	name = data[i][1]
# 	print(name)
# 	data.pop(i)
	#print("I am iiii: ", i)
	#print(emp_id)

#print(data)
	# for j in data:

	# 	if(j[0] == emp_id):

	# 		#print(j)

	# 		index2 = data.index(j)

	# 		print(count , '\t',emp_id, '\t', name, '\t', j[1], '\t', j[2], '\t', j[3])

	# 		count += 1

	# 		data.pop(index2)

	# if(count>4):

	# 	break
			
			

	

#print(data)

	
	# employee_id, name, salary, country, passcode = line.split("\t")
	# #curr_id, curr_name, curr_salary, curr_country, curr_passcode = employee_id, name, salary, country, passcode
	# if count == 0:
	# 	pass
	# else:
	# 	if name == '-' and count % 2 == 1:
	# 		# salary record
	# 		curr_id = employee_id
	# 		curr_salary = salary
		
	# 	else:
	# 		if name == "Name":
	# 			continue
			
	# 		else:
	# 			curr_name = name
	# 			print(curr_id, curr_name, curr_salary)	

	# # if count > 6:
	# # 	break

	# count +=1

#print(count)
	
#	print(words)
	
