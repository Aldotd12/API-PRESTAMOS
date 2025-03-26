import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.usersRoutes import user, auth_router
from routes.materialRoutes import material
from routes.loanRoutes import loan

app = FastAPI()

# Configurar CORS correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://frontsito-prestamos.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los headers
)

# Registrar las rutas después de configurar CORS
app.include_router(user)
app.include_router(auth_router)
app.include_router(material)
app.include_router(loan)

@app.get("/")
async def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render usa el puerto 10000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)
