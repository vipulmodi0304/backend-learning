# Lesson 6: Methods

## 1. Which method would you use for each: viewing your profile, signing up for a new account, changing only your profile picture, deleting a post?

GET, POST, PATCH, DELETE

## 2.What did the POST and DELETE return? Which family is that, and why do you think the server blamed itself instead of you?

Both returned code 501, which is server's fault. 501 means server code crashed.Because its an unsupported method?

## 3. What did /docs return, and where did the Location header send you? Same question for http://github.com.

Both gave code 301 which means location is somewhere else. Docs gave me location /docs/ github gave https.

## 4. 401 vs 403 in your own words, with your own example (not the club).

401 means server doesnt recognise me. 403 means server does recognise me but I am not allowed to access it. eg. 401 is like me showing up to a random person's house to sleepover. 403 is like me showing up to a friend's house but we have been fighting for a year so im not allowed to stay.

## 5. Your app returns a 500. Whose fault is it, and where would you look first?

it's server's fault. Server code failed. idk where to look.

## 6. Bonus, think about ReplayLab: it replays recorded requests. Why could replaying a recorded POST be risky in a way replaying a GET isn't?

if it contains an error it could breach the entire code get doesnt create anything new so we are safe just reading it.
