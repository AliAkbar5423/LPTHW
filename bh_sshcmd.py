import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_key('/home/ali/.ssh/known_hosts')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#untuk key auhentication dari .ssh
	client.connect(ip, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()
	#create connection
	if ssh_session.active:
		ssh_session.exec_command(command)
		print(ssh_session.recv(1024))
	return

	ssh_command('192.168.0.100','rafsan', 'testpython','id')
