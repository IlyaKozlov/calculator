from pathlib import Path

import uvicorn
from fastapi import FastAPI, Form
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from calculator import Calculator
from db.db_factory import get_db

app = FastAPI(title="Калькулятор")
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse(BASE_DIR / "templates" / "index.html")


@app.post("/calculations")
async def calculate(
    firstNumber: float = Form(),
    secondNumber: float = Form(),
    operation: str = Form(),
    sessionId: str = Form("default"),
) -> float:
    db = get_db()
    calculator = Calculator()
    operation = operation.strip()
    if operation == "+":
        result = calculator.add(firstNumber, secondNumber)
    elif operation == "-":
        result = calculator.subtract(firstNumber, secondNumber)
    elif operation == "*":
        result = calculator.multiply(firstNumber, secondNumber)
    elif operation == "/":
        try:
            result = calculator.divide(firstNumber, secondNumber)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=400, detail=f"Invalid operation {operation}")

    db.history_save(
        first_number=firstNumber,
        operation=operation,
        second_number=secondNumber,
        session_id=sessionId,
    )
    return result


@app.get("/history")
def get_history(
    operation: str | None = None, session_id: str | None = None
) -> list[dict]:
    db = get_db()
    return db.history_load(operation=operation, session_id=session_id)


@app.delete("/history")
def clear_history(session_id: str | None = None) -> dict[str, str]:
    db = get_db()
    db.history_clear(session_id=session_id)
    return {"status": "ok"}


@app.get("/favicon.ico")
def get_icon() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "favicon.ico")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1743)
