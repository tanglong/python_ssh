import paramiko
ssh = paramiko.SSHClient()
hostname = '182.254.208.180' 
myuser   = 'root'
mySSHK   = '/root/.ssh/id_rsa.pub'

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname, username=myuser, key_filename=mySSHK)

stdin, stdout, stderr = ssh.exec_command("""ls
ls
ls
""")
#print stdout.readlines()
print stdout.read()
ssh.close()

