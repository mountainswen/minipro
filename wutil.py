import random
import string
import os
import flask
root = './static/'

def Get_Extension(filename):
	return filename.rsplit('.',1)[1].lower()

def Get_Random_Str(n):
	ranstr = ''.join(random.sample(string.ascii_letters + string.digits,n))
	return ranstr

def Generate_ImageID():
	return Get_Random_Str(10)

def Generate_UserID(json_form):
	return json_form["nickName"]


def Insert_Into_DB(json_form):
	return 0

def Mkdir(UserID):
	#root = './Images/'
	path = root+UserID

	isExist = os.path.exists(path)
	
	if not isExist :
		os.makedirs(path)
		print 'mkdir successfully'
		#return 1

	return 0
def Check_User(UserID):
	path = root + UserID
	return not os.path.exists(path)
