

num = 3
password = 'a123456'

while num > 0:
	input_pwd = input('請輸入密碼: ')
	if input_pwd == password:
		print('輸入正確')
		break
	else:
		num = num - 1
		print('輸入錯誤, 請重複輸入: ')
		print('您還有', num, '次機會')
		