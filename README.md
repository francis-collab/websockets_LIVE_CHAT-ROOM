# 💬 Live WebSocket Chat Room

A lightweight real-time group chat app built with **Python WebSockets** on the backend and **vanilla HTML/CSS/JS** on the frontend — no frameworks, no fluff. Messages are broadcast instantly to all connected users, avatars are dynamically generated, and the interface is clean and responsive.

> 🔴 Real-time users  
> 📡 Live system messages  
> 🟢 Typing and sending with WebSockets  
> 👤 Avatar icons & clean UX  

---

## 📽 Demo

▶️ Watch the full demo here:  
[https://youtu.be/oX5qIR6MCNA](https://youtu.be/oX5qIR6MCNA)

---

## 🚀 Features

- 🔌 **Real-Time Chat** with WebSocket broadcasting  
- 🧑‍💼 Auto-generated emoji avatars per user  
- 🗨 Clean chat bubbles with name & timestamp  
- 🟢 Sidebar showing live online user list  
- 🔔 System messages for join/leave events  
- 💚 Sender vs receiver message styling  

---

## 🧱 Tech Stack

| Layer        | Tool/Library           |
|--------------|------------------------|
| Backend      | Python, `websockets`   |
| Frontend     | HTML, CSS, JavaScript  |
| Web Server   | Python’s built-in HTTP |
| Web Protocol | WebSocket (RFC 6455)   |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/live-websocket-chat.git
cd live-websocket-chat
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install websockets
```

### 3. Start the WebSocket server

```bash
python3 chat_server.py
```

### 4. In a new terminal tab, serve the frontend

```bash
python3 -m http.server 8000
```

### 5. Open the browser

```
http://localhost:8000/index.html
```

---

## 🖥️ How It Works

- When a user visits the page, they’re prompted for a name  
- A WebSocket connection is opened and the name is sent to the server  
- Server tracks all connected users, and notifies when someone joins or leaves  
- Chat messages are broadcast to all users in JSON format  
- Client dynamically renders:  
  - Sender’s name  
  - Avatar (based on first letter emoji)  
  - Colored bubble (green if it’s you)  
  - Timestamp (bottom right)  

---

## 📂 File Structure

```
.
├── chat_server.py     # WebSocket backend server
├── index.html         # Frontend UI + JS
└── README.md          # You're here!
```

---

## ✨ Customization Ideas

- Add persistent usernames with login  
- Allow switching between group chat rooms  
- Upload avatars or use profile initials  
- Integrate a database to store messages  
- Host frontend on GitHub Pages + server on Koyeb or Render  

---

## 👨‍💻 Author

**Francis**  
🛠️ Backend & WebSocket developer  
🌍 Kigali, Rwanda  
🎯 Building real-time apps and AI-driven tools

