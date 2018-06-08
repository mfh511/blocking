#!/usr/bin/env python
# -*- coding: utf-8 -*-
#头文件
import socket  
#说明当前运行的脚本为主程序
if "__main__" == __name__:   
  try:  
        #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个服务端
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);   
        #将套接字与指定的ip和端口相连
        sock.bind(('192.168.220.6', 3333));   
        #启动监听，并将最大连接数设为5       
        sock.listen(5);   
  #try中异常的时候执行except
  except:  
        print("init socket err!");  
  
  while True:  
        print("waiting for client...");
        #当有连接时，将接收到的套接字存到conn中，远程连接细节保存到addr中  
        conn, addr = sock.accept();
	#输出远程地址信息
        print("Accept new connection from");  
        print(addr);  
        while 1:
           #接受套接字的数据，数据以字符串形式返回，bufsize指定最多可以接收的数量
           szBuf = conn.recv(1024);  
           print("recv:" + szBuf);  
  	   #结束条件，套接字数据为0
           if szBuf == "0": 
               #将string中的数据发送到连接的套接字，返回值是要发送的字节数量
               conn.send('exit');
	       break
  	   else:
	       conn.send('welcome client!')
        #关闭套接字
        conn.close(); 
	print("end of sevice!")
