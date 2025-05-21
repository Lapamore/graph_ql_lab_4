import strawberry
from typing import AsyncGenerator
from backend.src.resolvers import Query, Mutation
from backend.src.models.strawberry_types import User
from backend.src.events.events_manager import event_manager

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_created(self) -> AsyncGenerator[User, None]:
        queue = event_manager.subscribe("user_created")
        try:
            while True:
                user = await queue.get()
                yield user
        finally:
            event_manager.unsubscribe("user_created", queue)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
) 