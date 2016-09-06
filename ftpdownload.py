from ftplib import FTP

port_num = 21
host_str = "ftpsite.vmware.com"
ftp = FTP(host_str)
ftp.set_debuglevel(1)
ftp.connect(host_str, port_num)
ftp.getwelcome()
ftp.login("inboundv", "J5WrfJG6")
print "==Getting DIR..."
lines = ftp.retrlines("LIST")
print "==Got DIR..."
print "Returned files list:\n", lines
ftp.cwd("/vra-assessment")
lines1 = ftp.retrlines("LIST")
print ">>>> inside assessment"
print lines1
