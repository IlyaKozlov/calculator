from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import uvicorn
from class_calculator import Calculator

app = FastAPI(title="Stub FastAPI App")


@app.get("/")
async def read_root():
    return {"status": "ok"}

@app.post("/calculations")
async def calculate(firstNumber: float, secondNumber: float, operation: str) -> float:
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1743)
