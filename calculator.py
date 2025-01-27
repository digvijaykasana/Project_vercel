# calculator.py
def handle_calculate(data):
    try:
        # Assuming the data is a simple mathematical expression in string form
        return str(eval(data))
    except Exception as e:
        return f"Error processing calculation: {str(e)}"
