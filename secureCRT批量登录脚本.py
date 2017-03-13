# $language = "python"
passwdfile='C:\\Users\\guohailan\\Desktop\\123.txt'
#crt.Dialog.MessageBox(host,"hostname",64|0)
def passwdlist(key_word):
	with open(passwdfile,'r') as f:
		for line in f:
			if key_word in line:
				return line	
def main():

    #进行cmd操作连接创建新的session连接
    cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /P 27836 /M MD5 %s" % (user, passwd, host)
    crt.Session.ConnectInTab(cmd)
    #使用默认弹窗提示信息
    #crt.Dialog.MessageBox('登录成功!')
def inputlist(userinput,separator):
	count=userinput.count(separator)
	hosts=userinput.split(separator, count)
	return hosts

userinput = crt.Dialog.Prompt("hostname","session","",False)

if ',' in userinput:
	hosts=inputlist(userinput,',')
	for host in hosts:
		passwdlist1=passwdlist(host)
		passwdlist2=passwdlist1.strip('\n')
		key=passwdlist2.split('|', 5)
		passwd=key[3]
		user=key[2]
		main()
elif '|' in userinput:
	hosts=inputlist(userinput,'|')
	host= hosts[0]
	passwd = hosts[3]
	user = hosts[2]
	main()
else:
	host=userinput
	passwdlist=passwdlist(host)
	passwdlist=passwdlist.strip('\n')
	key=passwdlist.split('|', 5)
	passwd = key[3]
	user = key[2]
	main()


