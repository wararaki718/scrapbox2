from fastapi import FastAPI

from routers import items

app = FastAPI()

# register routers
app.include_router(items.router)
