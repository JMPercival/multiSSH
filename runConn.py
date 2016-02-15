import conn
import sftp
import sys
from optparse import OptionParser

parser = OptionParser('Usage: %prog [options]')
parser.add_option('-a', '--all', dest='all', action='store_true', help='Run SSH on all servers')
parser.add_option('-g', '--generator', dest='generator', action='store_true', help='Run SSH on Generators')
parser.add_option('-p', '--power', dest='power', action='store_true', help='Run SSH on Power Stations')
parser.add_option('-r', '--relay', dest='relay', action='store_true', help='Run SSH on Relay')
parser.add_option('-c', '--center', dest='center', action='store_true', help='Run SSH on Centers')
parser.add_option('-l', '--list', type='string', dest='list', action='store', help='Run SSH on Comma Seperated List')
parser.add_option('-s', '--sftp', dest='sftp', action='store_true', help='Activate SFTP instead of commands')
(opts, args) = parser.parse_args()

logins = {'159.75.35.20':{'root':'10donuthack9'},
'159.75.35.21':{'root':'Top23named4'},
'159.75.35.31':{'root':'71stopthePower'},
'159.75.35.32':{'root':'shutMe66down'},
'159.75.35.42':{'root':'realWater94hulu'},
'159.75.35.41':{'root':'unreal61Gaming'},
'159.75.35.50':{'root':'pumpnIron856a'},
'159.75.35.51':{'root':'UcanthackTh1s'},
'159.75.35.52':{'root':'1amThePumkink1ng'},
'159.75.35.53':{'root':'pumping4Day555'},
'159.75.35.54':{'root':'doyouevenmavsec319'},
'159.75.35.55':{'root':'Drive42boxdrop'}
}
ip_to_host = {'159.75.35.20':'Power Control Center',
'159.75.35.21':'Treatment Center',
'159.75.35.31':'Generator 1',
'159.75.35.32':'Generator 2',
'159.75.35.42':'Relay 2',
'159.75.35.41':'Relay 1',
'159.75.35.50':'Power Station 0',
'159.75.35.51':'Power Station 1',
'159.75.35.52':'Power Station 2',
'159.75.35.53':'Power Station 3',
'159.75.35.54':'Power Station 4',
'159.75.35.55':'Power Station 5'
}
host_to_ip = {}
for ip in ip_to_host:
  host_to_ip[ip_to_host[ip]] = ip

hosts_to_connect = []
if opts.all:
  for host in host_to_ip:
    hosts_to_connect.append(host)
elif opts.generator:
  for host in host_to_ip:
    if 'Generator' in host:
      hosts_to_connect.append(host)
elif opts.power:
  for host in host_to_ip:
    if 'Power Station' in host:
      hosts_to_connect.append(host)
elif opts.relay:
  for host in host_to_ip:
    if 'Relay' in host:
      hosts_to_connect.append(host)
elif opts.center:
  for host in host_to_ip:
    if 'Center' in host:
      hosts_to_connect.append(host)
elif opts.list:
  for proposed_host in opts.list.split(','):
    for host in host_to_ip:
      if proposed_host == host:
        hosts_to_connect.append(proposed_host)

if len(hosts_to_connect) <= 0:
  print 'No hosts given...'
  sys.exit(0)

ips_to_connect=[]
for host in hosts_to_connect:
  ips_to_connect.append(host_to_ip[host])

shells = []
for ip in ips_to_connect:
  ip = ip
  user = logins[ip].keys()[0]
  passwd =  logins[ip][user]
  if opts.sftp:
    x = sftp.sftp(user, passwd, ip)
  else:
    x = conn.conn(user, passwd, ip)
  shells.append(x)
  print ip_to_host[ip]

command = raw_input("Command: ")
while(command != 'DONE'):
  for shell in shells:
    if opts.sftp:
      shell.runCommand(command)
    else:
      shell.runCommand(command)
      print shell.ip
      print shell.status
      print shell.stdout.read()
      print shell.stderr.read()
  command = raw_input("Command: ")

for shell in shells:
  shell.closeSocket()
