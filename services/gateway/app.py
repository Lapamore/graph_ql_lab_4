from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from backend.src.schemas.subscriptions import schema

graphql_app = GraphQLRouter(
    schema,
    subscription_protocols=["graphql-ws", "graphql-transport-ws"],
    graphiql=True
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "GraphQL API работает!", "graphql": "/graphql"} 