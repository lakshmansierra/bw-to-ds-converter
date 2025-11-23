import uvicorn
from fastapi import FastAPI
from api import upload_csv_route, convert_csv_route, view_json_route, download_json_route, list_json_route
from services.hana_service import get_hana_connection
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = get_hana_connection(print_schema=True, table_names=["file_bw_to_ds", "conversion_run_status_bw_to_ds", "conversion_status_bw_to_ds"])
    app.state.db = conn
    print("HANA DB connection established.")
    
    yield
    
    if hasattr(app.state, "db") and app.state.db:
        app.state.db.close()
        print("HANA DB connection closed.")

app = FastAPI(title="Bw to Ds Converter", lifespan=lifespan)

app.include_router(upload_csv_route.router, prefix="", tags=["csv"])
app.include_router(convert_csv_route.router, prefix="", tags=["conversion"])
app.include_router(view_json_route.router, prefix="", tags=["json"])
app.include_router(download_json_route.router, prefix="", tags=["json"])
app.include_router(list_json_route.router, prefix="", tags=["json"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bw to Ds Conversion API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
