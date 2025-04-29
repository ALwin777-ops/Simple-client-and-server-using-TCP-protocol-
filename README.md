# 🗨️ Python Socket Chat App (Client-Server Chat using TCP)

A simple terminal-based chat application using Python sockets. This project demonstrates a persistent TCP connection between a client and a server for real-time two-way messaging.

---

## 🎯 Features

### ✅ Two-Way Communication
- Enables real-time messaging between a server and a client over TCP.
- Messages can be sent back and forth like a mini chat app.

### ✅ Graceful Disconnect
- Type `bye` from either side to end the conversation cleanly.
- Both server and client handle the disconnect smoothly.

### ✅ Lightweight & Beginner-Friendly
- Uses only Python's built-in `socket` library.
- Great for learning the basics of networking.

---

## 🚀 How It Works

### 1️⃣ TCP Sockets:
- The server binds to a port and listens for incoming connections.
- The client connects to the server's IP and port using TCP.
- A loop enables continuous exchange of messages.

### 2️⃣ Communication Flow:
- Each side sends and receives messages using `send()` and `recv()`.
- UTF-8 encoding is used for data transfer.

### 3️⃣ Termination:
- Either user can type `bye` to close the socket and end the chat.

---

## 🛠️ Requirements

- Python 3.x
(No third-party libraries required)

---

## 💻 How to Run

### 1. Clone the Repository:
```bash```
- git clone https://github.com/your-username/python-socket-chat.git. 
- cd python-socket-chat
### 2. Run the Server.
- python server.py.
### 3. In another terminal, run the Client:.
- python client.py.
