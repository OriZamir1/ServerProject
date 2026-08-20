# Multi-Client Chat App

A terminal-based chat application built with Python sockets and threading — 
supports multiple simultaneous clients, real-time broadcasting, and join/leave 
notifications, using only Python's standard library .

## Features

- **Real-time two-way messaging** — threading allows users to send and receive messages simultaneously.
- **Username support** — users enter a username on connect, receive a greeting, and every message is tagged with their name.
- **Join/leave notifications** — other users are notified when someone connects or disconnects.
- **Graceful disconnect handling** — abrupt disconnects (e.g. closing the window instead of typing "quit") are caught and handled cleanly, preventing server crashes.
- **Concurrent client handling** — each connected client is managed in its own thread on the server, supporting multiple simultaneous users.
- **Built with Python's standard library only** — no external networking frameworks, just `socket` and `threading`.

## How It Works

The server acts as a central relay — it connects clients and broadcasts 
messages between them. Each connected client runs on its own thread on 
the server, which allows multiple users to send and receive messages at 
the same time without blocking each other.

Messages are encoded into bytes before being sent over the socket, and 
decoded back into text when displayed. The server itself never decodes 
messages — it treats them as raw bytes and simply forwards them, since 
its only job is to relay, not to read or process content.

Usernames are handled client-side: each message is prefixed with the 
sender's username before being sent (e.g. "Alice: hello"), so the server 
doesn't need to attach it. Separately, the server keeps a dictionary 
mapping each connected socket to its username, used to broadcast 
join/leave notifications.

## How to Run

1. Run the server:
```
python server.py
```
2. Run as many clients as you'd like, each in a separate terminal:
```
python client.py
```
3. When a client connects, you'll be prompted to enter a username — 
   this is shown next to your messages so others know who's chatting.
4. To exit as a client, type `quit`.

## What I Learned

- **Threading:** I learned why threads are necessary for real-time, 
  two-way communication — since `recv()` and `input()` both block 
  (pause the program while waiting), a single thread can't handle 
  sending and receiving at the same time. Running them in separate 
  threads lets both happen simultaneously.
- **Data structures matter:** Once I added usernames, I had to switch 
  from a list to a dictionary to track which socket belonged to which 
  user — this made it possible to broadcast join/leave messages by 
  name instead of just a raw socket or address.
- **Encoding vs. encryption:** I initially assumed converting messages 
  to bytes (`encode()`/`decode()`) was a form of encryption. I learned 
  it's actually just a format conversion between text and bytes — real 
  encryption would require actually transforming the content to hide 
  it, which this project doesn't do.