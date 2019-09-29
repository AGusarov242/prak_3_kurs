alphabet = ['_', '!', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def combinator(number):
	''' .... return all combinations of symbols on telephone(of each number)
	   for telephone number(which is an argument) .... '''
	''' .... '_' and '!' is my indication of required symbols .... '''
	tel_len = len(number)
	all_combinations = ['']
	for i in range(tel_len):
		all_combinations = [all_combinations + j for all_combinations in all_combinations
		    for j in str(alphabet[int(number[i])])]
	return all_combinations

tel_number = "79197601781"
print(combinator(tel_number))