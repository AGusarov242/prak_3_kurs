text = input()
list_of_words = text.split()
my_dictionary = [['', 0] for i in range(len(list_of_words))]
max_count = 1
max = ['', 0]
for i in range(len(list_of_words)):
	for k in range(len(list_of_words)):
		if my_dictionary[k][0] == list_of_words[i]:
			my_dictionary[k][1] = int(my_dictionary[k][1]) + 1
			break
		if str(a[k][0]) == '':
			my_dictionary[k][0] = list_of_words[k]
			my_dictionary[k][1] = 1
			break
	if int(my_dictionary[k][1]) > int(max[1]):
		max[0] = my_dictionary[k][0]
		max[1] = my_dictionary[k][1]
		max_count = 1
	elif int(a[k][1]) == int(max[1]):
		max_count += 1
if max_count == 1:
	print(max[0])
else:
	print('-')