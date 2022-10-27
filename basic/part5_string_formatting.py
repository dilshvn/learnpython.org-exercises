data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s.".format(data[0],data[1],str(data[2]))

print(format_string)