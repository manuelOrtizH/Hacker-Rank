#Manuel Ortiz Hernández at 2020
#Python Problems. Extracted from: https://www.hackerrank.com/challenges/finding-the-percentage/problem

def get_average(student_marks, query_name):
	average = 0
	total_marks = len(student_marks[query_name])
	for marks in student_marks[query_name]:
		average+=marks/total_marks

	return average


if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float,line))
		student_marks[name]= scores
	query_name = input()

    average  = get_average(student_marks, query_name)
    print("{:0.2f}".format(average))


	


