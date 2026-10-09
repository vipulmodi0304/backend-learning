# Lesson 7 Headers

## 1.What are headers for?

Headers are used to get information about the message that is being communicated between client and server.

## Which headers did curl add automatically in step 1?

Host, User-Agent, and accept

## Why did page.html and page.txt look different in Edge when the content was identical?

Because of content type. One is html one is plain text.

## Your made-up X-My-Name header showed up on httpbin. What does that tell you about who decides header names?

it tells me that client can choose header name.

## Why does a server need the Host header if the request already reached its IP?

Because an IP can have several hosts. So to specify which one we need.

## Which header carries proof of who you are, and which status code would you expect if it’s missing?

The Authorization header carries proof of who you are, usually through a token or username and password.
If it's missing and authentication is required, you'd typically expect 401 Unauthorized.

## What did Edge send to httpbin that curl didn’t?

idk
