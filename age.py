driving = input('請問有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit

age = input('請問你的年紀? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('這年紀可以開車嗎?')
elif driving == '沒有':
	if age >= 18:
		print('建議可以去考駕照了')
	else:
		print('再過幾年就可以考駕照了')



