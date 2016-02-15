from paramiko import Transport
from paramiko import SFTPClient

class sftp():
  def __init__(self, user, passwd, ip):
    self.ip = ip
    try:
      t = Transport((ip, 22))
      t.connect(username = user, password = passwd)
      self.sftpObject = SFTPClient.from_transport(t)
      self.status = 'Success'
    except:
      self.status = 'Failed'

  def runCommand(self, command):
    command = command.split()
    if command[0] == 'pwd':
      print self.sftpObject.getcwd()
    elif command[0] == 'ls':
      try:
        print self.sftpObject.listdir(command[1] if len(command) > 1 else '.')
      except:
        print 'No such file'
    elif command[0] == 'cd':
      try:
        print self.sftpObject.chdir(command[1] if len(command) > 1 else '/')
      except:
        print 'No such file'
    elif command[0] == 'mkdir':
      print self.sftpObject.mkdir(command[1] if len(command) > 1 else '')
    elif command [0] == 'put':
      print self.sftpObject.put(command[1], command[2])
    elif command[0] == 'get':
      print self.sftpObject.get(command[1], command[2]+'.'+self.ip)
    elif command[0] == 'rm':
      try:
        print self.sftpObject.remove(command[1])
      except:
        print 'No such file'

  def closeSocket(self):
    self.sftpObject.close()

  def getcwd(self):
    self.sftpObject.getcwd()

  def listdir(self, path='.'):
    self.sftpObject.listdir(path)

  def chdir(self, path='/'):
    self.sftpObject.chdir(path)

  def mkdir(self, path, mode=511):
    self.sftpObject.mkdir(path, mode)

  def normalize(self, path):
    self.sftpObject.normalize(path)

  def put(self, localpath, remotepath, callback=None, confirm=True):
    self.sftpObject.put(localpath, remotepath, callback, confirm)

  def get(self, remotepath, localpath, callback=None):
    self.sftpObject.get(remotepath, localpath, callback)

  def remove(self, path):
    self.sftpObject.remove(path)

