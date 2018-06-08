#!/usr/bin/env python
# -*- coding: utf-8 -*-
#头文件
import socket;   
#说明当前运行的脚本为主程序  
if "__main__" == __name__:  
    #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  
    #连接到服务器
    sock.connect(('192.168.220.6', 3333));    
    while 1:
	#把输入的值赋值给data
        data = raw_input('please input work: ')
	#发送数据
        sock.send(data)
	#接受数据（前一步输入的），数据以字符串形式返回并打印
        print sock.recv(1024)
	#如果接收到的字符是“exit”,就停止
        if data == 'exit':
            break
    #关闭套接字
    sock.close()    
    print("end of connect"); 
