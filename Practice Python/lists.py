#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/python-lists/problem
def read_data():
	N = int(input())
	list_to_modify = []
	for _ in range(N):
		commands = {}
		function, *line = input().split()
		numbers = list(map(str, line))
		commands[function] = numbers
		det_cmds(commands, list_to_modify)
		
	return commands

def det_cmds(commands, list_to_modify):
	for function, numbers in commands.items():
		if function == "print":
			print(list_to_modify)
		else:
			function += "(" + ",".join(numbers) + ")"
			eval("list_to_modify."+function)
		
read_data()