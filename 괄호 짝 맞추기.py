def func(s):
	st = []
	for i in s:
		if i == "(" or i == "[" or i == "{":
			st.append(i)
		elif i == ")":
			if "(" == st[-1]:
				st.pop()
			else:
				return False
		elif i == "}":
			if "{" == st[-1]:
				st.pop()
			else:
				return False
		elif i == "]":
			if "[" == st[-1]:
				st.pop()
			else:
				return False
	if len(st):
		return False
	return True
s = input()
print(func(s))
