from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import analytics, csv_import
from routes.assignment import router as assignment_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lead Analytics Dashboard API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Existing routers
app.include_router(analytics.router, prefix="/api", tags=["analytics"])
app.include_router(csv_import.router, prefix="/api", tags=["csv"])

# NEW Assignment Router (Lead Assignment Engine)
app.include_router(assignment_router, tags=["assignment"])


@app.get("/")
def root():
    return {"message": "Lead Analytics API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}