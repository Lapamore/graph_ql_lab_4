from backend.src.models.strawberry_types import Role, User


users = [
    User(id="1", email="Dima@example.com", name="Dima", role=Role.USER),
    User(id="2", email="Maks@example.com", name="Maks", role=Role.ADMIN),
    User(id="3", email="Emil@example.com", name="Emil", role=Role.USER),
    User(id="4", email="Gosha@example.com", name="Gosha", role=Role.ADMIN),
    User(id="5", email="Damir@example.com", name="Damir", role=Role.USER),
    User(id="6", email="frank@example.com", name="Frank", role=Role.USER),
    User(id="7", email="grace@example.com", name="Grace", role=Role.ADMIN),
    User(id="8", email="henry@example.com", name="Henry", role=Role.USER),
    User(id="9", email="irene@example.com", name="Irene", role=Role.USER),
    User(id="10", email="jack@example.com", name="Jack", role=Role.ADMIN)
]
