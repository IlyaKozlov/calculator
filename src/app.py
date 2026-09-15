import uvicorn
from fastapi import FastAPI, Form
from fastapi.exceptions import HTTPException

from calculator import Calculator
from db.db_factory import get_db

app = FastAPI(title="Stub FastAPI App")


@app.get("/")
async def read_root():
    return {"status": "ok"}


@app.post("/calculations")
async def calculate(
    firstNumber: float = Form(), secondNumber: float = Form(), operation: str = Form()
) -> float:
    db = get_db()
    db.history_save(
        first_number=firstNumber, operation=operation, second_number=secondNumber
    )

    calculator = Calculator()
    operation = operation.strip()
    if operation == "+":
        return calculator.add(firstNumber, secondNumber)
    if operation == "-":
        return calculator.subtract(firstNumber, secondNumber)
    if operation == "*":
        return calculator.multiply(firstNumber, secondNumber)
    if operation == "/":
        try:
            return calculator.divide(firstNumber, secondNumber)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=400, detail=f"Invalid operation {operation}")


@app.get("/history")
def get_history() -> list[dict]:
    db = get_db()
    return db.history_load()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1743)
