#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
	line = line.split(" ")
	#new_line = line.split(" ") Split all the line
	new_line = "-".join(line)
	return new_line

if __name__ == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)