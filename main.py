from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



from routers import login
app.include_router(login.router)


from routers import home
app.include_router(home.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
