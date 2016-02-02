def main():
	print "\t.data"
	
	lines = open("test1.tac","r").readlines()
	identifiers = {}
	arrays = {}

	for line in lines:
		line = line.split()
		if line[1] in ['+','-','/','*','%','&','|','^']:
			if line[2] not in identifiers:
				identifiers[line[2]]=1
		elif line[1]=='=':
			if(['&','*','['] not in line):
				if line[2] not in identifiers:
					identifiers[line[2]]=1
			elif line[-1]==']':
				if line[2] not in identifiers:
					identifiers[line[2]]=1
			elif line[3] in ['&','*'] :
				if line[2] not in identifiers:
					identifiers[line[2]]=1
			elif line[2] == '*':
				if line[3] not in identifiers:
					identifiers[line[3]]=1
		elif line[1]== 'Array':
			if line[2] not in arrays:
				arrays[line[2]] = line[3]
	for identifier in identifiers:
		print identifier + ":\t.word\t0"
	for array in arrays:
		print array + ":\t.space\t" + str(arrays[array])

if __name__ == '__main__':
	main()