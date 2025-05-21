import strawberry
from typing import List, Optional
import uuid

from backend.src.models.strawberry_types import User, Token, UserInput, LoginInput, Role
from backend.src.events.events_manager import event_manager
from backend.src.mocks.users import users


@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, id: str) -> Optional[User]:
        for user in users:
            if user.id == id:
                return user
        return None

    @strawberry.field
    def get_users(self) -> List[User]:
        return users

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, user_input: UserInput) -> User:
        user = User(
            id=str(uuid.uuid4()),
            email=user_input.email,
            name=user_input.name,
            role=Role.USER
        )
        users.append(user)
        await event_manager.publish("user_created", user)
        return user

    @strawberry.mutation
    def login(self, login_input: LoginInput) -> Token:
        for user in users:
            if user.email == login_input.email:
                return Token(
                    access_token="access",
                    refresh_token="refresh"
                )
        raise Exception("Invalid credentials") 