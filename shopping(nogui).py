shuiguo={'苹果':'5','香蕉':'4','桃子':'7','梨':'6'}
import time

print("-"*37)
while True:
	print("欢迎使用没卵用的电商汐桶")
	print("本店仅售苹果，香蕉，桃子和梨")
	print("温馨xio提醒：“还要继续购买吗？”使用是/否来回答")
	a=input('您要购买什么？：')
	if a in shuiguo:
		aa=int(shuiguo[a])
		print(f'{a}的价格为：{aa}')
		b=int(input('数量是？：'))
		c=input('还要继续购买吗？：')
		if c=="是":
			d=input('您要购买什么？：')
			if d in shuiguo:
				e=int(shuiguo[d])
				print(f'{d}的价格为{e}')
				f=int(input('数量是？：'))
				g=input('还要继续购买吗？：')
				if g=="是":
					h=input('您要购买什么？：')
					if h in shuiguo:
						i=int(shuiguo[h])
						print(f'{h}的价格为{i}')
						j=int(input('数量是？：'))
						k=input('还要继续购买吗？：')
						if k=="是":
							l=input('您要购买什么？：')
							if l in shuiguo:
								m=int(shuiguo[l])
								print(f'{l}的价格为{m}')
								n=int(input('数量是？：'))
							elif l not in shuiguo:
								print("error!")
								time.sleep(2)
						elif k=="否":
							score=b*aa+e*f+i*j
							print(f'共{score}元，已自动付款！')
							print("-"*37)
							input('请按enter退出')
							break
					elif h not in shuiguo:
						print("error")
						time.sleep(2)
				elif g=="否":
					score=b*aa+e*f
					print(f'共{score}元，已自动付款！')
					print("-"*37)
					input('请按enter退出')
					break
			elif d not in shuiguo:
				print("error")
				time.sleep(2)
		elif c=="否":
			score=b*aa
			print(f'共{score}元，已自动付款！')
			print("-"*37)
			input('请按enter退出')
			break
	elif a not in shuiguo:
		print("error")
		time.sleep(2)
	
	score=b*aa+e*f+i*j+m*n
	print(f'共{score}元，已自动付款！')
	print("-"*37)
	input('请按enter退出')
	break
