import sys

for line in sys.stdin:
	try:
	
		#employee_id = "-"
		# name = "-"
		# salary = "-"
		# country = "-"
		# passcode = "-"
		
		line = line.strip()
		linesplit = line.split("\t")

		#print(linesplit)	
		
		if len(linesplit) == 2:
			# only id and name
			if "Employee" in linesplit[0]:
				pass
			else:
				employee_id = linesplit[0]
				name = linesplit[1]
				print("%s\t%s"%(employee_id, name))		
		else:
			if "Employee" in linesplit[0]:
				pass
			# id, salary, country, passcode
			elif len(linesplit) == 5:
				# where only dollars value are separated
				employee_id = linesplit[0]
				salary = linesplit[1] + linesplit[2]
				country = linesplit[3]
				passcode = linesplit[4]
				print("%s\t%s\t%s\t%s" % (employee_id, salary, country, passcode))
				
			elif len(linesplit) == 6:
				# dollars and country both separated
				employee_id = linesplit[0]
				salary = linesplit[1] + linesplit[2]
				country = linesplit[3] + linesplit[4]
				passcode = linesplit[5]
				print("%s\t%s\t%s\t%s" % (employee_id, salary, country, passcode))

			
		if '-' in employee_id:
			pass
		
		#print("%s\t%s\t%s\t%s\t%s" % (employee_id, name, salary, country, passcode))

	except:
		pass

#	employee_id = linesplit[0]
#	name = linesplit[1]
#	salary = linesplit[2]
#	country = linesplit[3]
#	passcode = linesplit[4]
	
#	print("%s\t%s\t%s\t%s" % (employee_id, name,salary, country))
	
	# \t%s\t%s\t%s
	# , salary, country, passcode
