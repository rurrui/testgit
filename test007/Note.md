hello.txt是一个三行的文本文件  
在windows下，每行的结尾是由\r\n表示的  
使用open(url,rt)的时候会把读出来的\r\n替换为\n  
当open(url,w)就会随平台再把\r\n写回去