#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������o
���ڣ�2020.4.8
"""

import random



def name_to_number(name):
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error:No Correct Name")



def number_to_name(number):
	if number==0:
		return "ʯͷ"
	if number==1:
		return "ʷ����"
	if number==2:
		return "ֽ"
	if number==3:
		return "����"
	if number==4:
		return "����"
	else:
		print("Error:No Correct Name")

 
import random

def rpsls(player_choice):
	print("--------")
	print("����ѡ��Ϊ:",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,4)
	comp_choice=number_to_name(comp_number)
	print("�������ѡ��Ϊ:",comp_choice)
	r=(player_number-comp_number)%5
	if r==1 or r==2:
		print("��Ӯ��")
	if r==3 or r==4:
		print("�����Ӯ��")
	if r==0:
		print("���ͼ��������һ����")
	else:
		print("Error")


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


