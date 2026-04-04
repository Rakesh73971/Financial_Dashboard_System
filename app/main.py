from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import auth,transactions,dashboard
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limiter import limiter



app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(dashboard.router)