#Lesson 3: local host and ports

##1. What does localhost mean?
It's just a name for the IP address of my own laptop

##2. What is a port?
a port is the number that tells the computer which program a message is for.

##3. Why did the 9000 command fail in terminal 2?
port 9000 was already bound by the program in terminal 1, and that program didn't allow sharing, so the second bind failed.

##4. Why don't you type :443 when you visit google.com?
HTTPS always uses 443 by default, so the browser assumes it. If a site ran on a different port, you'd have to type it, exactly like :8000.
