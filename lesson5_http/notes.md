# Lesson 5: HTTP

# 1. What is HTTP?

Way of communication between programs. Clients and servers. its just plain text with a strict layout

# 2. Name the four parts of a request and of a response.

Request line,header,blank line,body

# 3. How does the server know your headers are finished?

through blank line

# 4. Find the Content-Length header in your output. What does that number mean? Check it against hello.txt.

it is the number of characters in the txt file

# 5. What changed in the raw response for /nope.txt?

file not found. Error 404.

# 6. Your script, curl, and Edge are very different programs. Why can the same server answer all three?

The server does not know which program sent the request. It only sees the HTTP message: the request line, headers, and blank line. Your script wrote this message manually. curl creates it automatically. Edge creates it automatically too. Different programs can send the request, but they all follow the same HTTP format. So, to the server, they all look like the same type of message. This is why HTTP being a standard is important.
