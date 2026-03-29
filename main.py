from fastapi import FastAPI

# Initialize the API
app = FastAPI(title="Edge AI Math Engine")

# The function your Agents wrote!
def calculate_fibonacci(n: int):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current

# Route 1: The Homepage
@app.get("/")
def home():
    return {"message": "Welcome to the Production API. System is online."}

# Route 2: The Action Endpoint
@app.get("/api/fibonacci/{number}")
def get_fib_number(number: int):
    # Calculate it
    result = calculate_fibonacci(number)
    
    # Return a clean JSON response
    return {
        "requested_n": number,
        "fibonacci_result": result,
        "status": "success"
    }