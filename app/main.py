from fastapi import FastAPI
from app.auth.routes import router as authRouter
from app.db.database import Base, engine

# IMPORTANT: import models so SQLAlchemy sees them
from app.users import models as user_models

app = FastAPI(
    title="Expense Tracker API",
    version="1.0.0"
)

# Create all tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Expense Tracker API running 🚀"}


app.include_router(authRouter)
