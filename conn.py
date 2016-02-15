import sys
try:
  from paramiko import SSHClient
  from paramiko import AutoAddPolicy
  from paramiko import SFTPClient
except ImportError:
  print 'Missing Paramiko Dependency.'
  sys.exit(0)

class conn():
  def __init__(self, user, passwd, ip):
    self.user = user
    self.passwd = passwd
    self.ip = ip
    
    self.sshConn = SSHClient()
    self.sshConn.set_missing_host_key_policy(AutoAddPolicy())

    try:
      self.sshConn.connect(self.ip, port = 22, 
        username = self.user,password = self.passwd, 
        timeout = 60, allow_agent = False,look_for_keys = False)
          
      self.status = 'Succeeded'
    except:
      self.status = 'Failed'

  def runCommand(self, command):
    self.stdin, self.stdout, self.stderr = (None,None,None)
    if self.status == 'Succeeded':
      self.stdin, self.stdout, self.stderr = self.sshConn.exec_command(command)
   
  def closeSocket(self):
    self.sshConn.close()
