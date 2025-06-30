import asyncio
import json
from websockets import serve

connected_users = {}  # websocket: username

async def notify_user_list():
    user_list = list(connected_users.values())
    payload = {"type": "user_list", "users": user_list}
    await broadcast(payload)

async def notify_system(message):
    payload = {"type": "system", "message": message}
    await broadcast(payload)

async def broadcast(data):
    msg = json.dumps(data)
    to_remove = set()
    for ws in connected_users:
        try:
            await ws.send(msg)
        except:
            to_remove.add(ws)
    for ws in to_remove:
        connected_users.pop(ws, None)

async def handler(websocket):
    try:
        # First message must include the username
        raw = await websocket.recv()
        hello = json.loads(raw)

        if hello.get("type") != "hello" or "name" not in hello:
            await websocket.close()
            return

        username = hello["name"]
        connected_users[websocket] = username

        print(f"✅ {username} connected")
        await notify_user_list()
        await notify_system(f"🟢 {username} joined the chat")

        async for msg in websocket:
            data = json.loads(msg)
            if data.get("type") == "chat":
                print(f"💬 {data['name']}: {data['message']}")
                await broadcast(data)

    finally:
        if websocket in connected_users:
            left_user = connected_users.pop(websocket)
            print(f"❌ {left_user} disconnected")
            await notify_user_list()
            await notify_system(f"🔴 {left_user} left the chat")

async def main():
    async with serve(handler, "localhost", 8001):
        print("🟢 Server running at ws://localhost:8001")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

