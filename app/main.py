from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import auth,records,dashboard
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.core.limiter import limiter



app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(records.router)
app.include_router(dashboard.router)