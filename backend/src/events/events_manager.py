from typing import AsyncGenerator, Dict, List
import asyncio
from backend.src.models.strawberry_types import User

class EventManager:
    def __init__(self):
        self._subscribers: Dict[str, List[asyncio.Queue]] = {
            "user_created": []
        }
        self._lock = asyncio.Lock()

    async def publish(self, event_type: str, data: User):
        async with self._lock:
            if event_type in self._subscribers:
                for queue in self._subscribers[event_type]:
                    try:
                        await queue.put(data)
                    except Exception as e:
                        print(f"Error publishing to queue: {e}")

    def subscribe(self, event_type: str) -> asyncio.Queue:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        queue = asyncio.Queue()
        self._subscribers[event_type].append(queue)
        return queue

    def unsubscribe(self, event_type: str, queue: asyncio.Queue):
        if event_type in self._subscribers:
            try:
                self._subscribers[event_type].remove(queue)
            except ValueError:
                pass

event_manager = EventManager() 