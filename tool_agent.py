from baml_client import b
from baml_client.types import WeatherAPI, CalculatorAPI

# def handle_weather(weather: WeatherAPI):
#     # Simulate weather API call, but you can implement this with a real API call
#     return f"The weather in {weather.city} at {weather.time} is sunny."

# def handle_calculator(calc: CalculatorAPI):
#     numbers = calc.numbers
#     if calc.operation == "add":
#         result = sum(numbers)
#     elif calc.operation == "subtract":
#         result = numbers[0] - sum(numbers[1:])
#     elif calc.operation == "multiply":
#         result = 1
#         for n in numbers:
#             result *= n
#     elif calc.operation == "divide":
#         result = numbers[0]
#         for n in numbers[1:]:
#             result /= n
#     return f"The result is {result}"

def main():
    print("Agent started! Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Call the BAML function to select tool
        tool_response = b.SelectTool(user_input)

        # Handle the tool response
        if isinstance(tool_response, WeatherAPI):
            result = tool_response
            print(f"Agent (Weather): {result}")
        
        elif isinstance(tool_response, CalculatorAPI):
            result = tool_response
            print(f"Agent (Calculator): {result}")

if __name__ == "__main__":
    main()
