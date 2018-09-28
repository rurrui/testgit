# I/O读写问题
hello.txt是一个三行的文本文件  
在windows下，每行的结尾是由\r\n表示的  
使用open(url,rt)的时候会把读出来的\r\n替换为\n  
当open(url,w)就会随平台再把\r\n写回去  
# Json的问题  
1.在python中创建的对象是运行时对象  
2.如果想把运行时对象存储到存储设备上时，必须先进行序列化操作  
3.JSON Moudle有一个dumps方法，这个方法可以把一个python对象序列化为json数据格式然后存储   
4.dump(object,file)这个方法可以直接把object序列化，并且写入一个text file文件对象中  
5.json.load(f)可以反序列化文件对象中的存储  
# 输出的显示问题
1.在py命令行中直接键入某一个对象，输出会显示为机器识别的对象  
2.print打印会以人类识别模式读取
