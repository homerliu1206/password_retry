ans = 'a123456'
x = 3 #剩餘機會

while True:
	pwd = input ('請輸入密碼:')

	if  pwd == ans:
		print ('登入成功!')
		break #逃出迴圈
	else:
		x = x - 1 #嘗試錯誤後少一次機會
		print ('密碼錯誤!還有',x , '次機會')
		if x == 0:
			print ('請15分鐘後再嘗試')
			break