import socket

# 1. Make a socket (Your program's plug into the network)
s = socket.socket()

# 2. Connect to the server: IP + port (no DNS needed, it's localhost)
s.connect(("127.0.0.1", 8000))

# 3. Write an http request as plain text
# \r\n is how http ends each line 
request = (
"GET /hello.txt HTTP/1.1\r\n"
"Host: localhost\r\n"
"Connection: close\r\n"
"\r\n"
)

# 4. Send it. Networks send bytes, not text so .encode() converts it. 
s.sendall(request.encode())

# 5.  Read the response in chunks until the server hangs up
response = b""
while True:
  chunk = s.recv(4096)
  if not chunk:
    break
  response += chunk
  
s.close()

# 6. Convert bytes back to text and print it
print(response.decode())
