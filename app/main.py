from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.image_gen import gen_image
# 1. Initialize the FastAPI app
app = FastAPI(
    title="Image Generation Backend",
    version="1.0.0"
)

# 2. Configure CORS (Crucial if your frontend connects from a different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains (e.g., ["http://localhost:3000"]) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Include the endpoints from your api folder
app.include_router(gen_image, prefix="/api")

# 4. Optional: Root health-check endpoint
@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to the Image Gen API"}
