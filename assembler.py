def simple_assembler(program):
	# return a dictionary with the registers
	variable_vals = {}
	for i in program:
		command_val = i.split()
		if command_val[0] == 'mov':
		    globals () [command_val[1]] = int(command_val[2])
		    variable_vals[command_val[1]]=eval(command_val[1])
		elif command_val[0] == 'inc':
			variable_vals[command_val[1]] = variable_vals[command_val[1]]+1
		elif command_val[0] == 'dec':
			variable_vals[command_val[1]] = variable_vals[command_val[1]]-1
		else:
			if eval(command_val[1])!=0:
				

	return variable_vals


code = '''\
mov a 5
inc a
inc a
dec a
mov b 16
inc a
dec b
inc a
dec a
dec a
'''

print(simple_assembler(code.splitlines()))