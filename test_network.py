import nmap 

nm = nmap.PortScanner() 

cidr2 = '192.168.1.1/24'
a=nm.scan(hosts=cidr2, arguments='-sP') 
path = './devices.txt'
file=open(path,'w')



for k,v in a['scan'].items(): 
    if str(v['status']['state']) == 'up':
#        print( str(v))
        try:
          print(v)
#        	if 'Tp-link Technologies' in str(v['vendor']):
#        		file.write( str( v['addresses']['ipv4']) + ' ' + str(v['vendor']) + '\n')    
#          print( str(" v['addresses']['ipv4']) + ' => ' + str(v['addresses']['mac'] + str(v['vendor'])))
        except:
#          print("error")
          print( str(v['addresses']['ipv4']))

file.close()
