from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material import Material
from app.utils.auth import get_current_user
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

router = APIRouter(tags=["forecast"])


@router.get("/forecast")
def forecast(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    materials = db.query(Material).all()
    result = []
    for material in materials:
        if material.quantity <= 0:
            continue
        x = np.array([[i] for i in range(6)]).reshape(-1, 1)
        y = np.array([max(material.quantity - i * 5, 0) for i in range(6)])
        model = LinearRegression()
        model.fit(x, y)
        future = float(model.predict(np.array([[6]]) )[0])
        result.append({
            "name": material.name,
            "current_stock": material.quantity,
            "predicted_stock": round(max(future, 0), 2),
            "depletion_date": "Within 1 month" if future <= 0 else "Next month",
        })
    return {"forecast": result}
