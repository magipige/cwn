#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈婉薿
日期：2020.4.8
"""

import random



def name_to_number(name):
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="纸":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error:No Correct Name")



def number_to_name(number):
	if number==0:
		return "石头"
	if number==1:
		return "史波克"
	if number==2:
		return "纸"
	if number==3:
		return "蜥蜴"
	if number==4:
		return "剪刀"
	else:
		print("Error:No Correct Name")

 
import random

def rpsls(player_choice):
	print("--------")
	print("您的选择为:",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,4)
	comp_choice=number_to_name(comp_number)
	print("计算机的选择为:",comp_choice)
	r=(player_number-comp_number)%5
	if r==1 or r==2:
		print("您赢了")
	if r==3 or r==4:
		print("计算机赢了")
	if r==0:
		print("您和计算机出的一样呢")
	else:
		print("Error")


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


