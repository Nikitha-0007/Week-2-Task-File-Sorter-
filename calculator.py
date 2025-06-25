import os
import logging
from db_helper import log_operation

# ✅ Ensure 'logs' directory exists before logging
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# ✅ Set up logging
log_file = os.path.join(log_folder, 'operation_log.txt')
logging.basicConfig(filename=log_file, level=logging.INFO)

def calculate():
    while True:
        try:
            expr = input(">> ")
            if expr.lower() == 'exit':
                break
            result = eval(expr)
            print("Result:", result)
            log_operation(expr, result)
            logging.info(f"{expr} = {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print("Invalid input:", e)

if __name__ == "__main__":
    calculate()
