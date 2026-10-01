## Lesson 4 IP Address and DNS

# What is an IP Address?

Every device connected to internet has a numeric address which is its IP address

# What does DNS do?

It is like the contact book for the IP addresses. You ask DNS for an address for any computer on the internet and it gives you back the numbers.

# Why doesn't localhost need DNS?

It doesnt need DNS because we already have the numbers for our own computer and dont need to find them through dns we can go directly to step 2 which is connecting to IP and port.

# Why did https://1.1.1.1 work without a name?

It doesnt need a name to work. Name is just to make IP convinient. if we already have the IP we dont need to ask dns for a name.

# The fake domain error vs the localhost:8002 error from last lesson: which step in the diagram failed in each case?

fake domain error failed in step 1 because no such device exists whose DNS is that. localhost:8002 failed on step 2 where we did get the IP and port from dns but nothing was connected to the port so no program to run.
