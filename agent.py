from baml_client import b
from baml_client.types import Steps, Answer


def generate_plan(user_input: str, available_functions) -> list[Steps]:
    # user_input = input("Please describe the problem: ")

    plan = b.GeneratePlan(user_input, available_functions=available_functions)
    print(f"Plan: {plan}")

    return plan

def execute_plan(plan: list[Steps], tools: list) -> Answer:

    # Execute the plan
    result = 0
    updated_input = ""
    for index, step in enumerate(plan):
        if isinstance(step, Steps):
        
            function_name = step.function_name
            input = updated_input + step.step
            print(f"\n Input: {input}")
            if function_name == "Add" and function_name in tools:
                result = b.Add(input)
            elif function_name == "Subtract" and function_name in tools:
                result = b.Subtract(input)
            elif function_name == "Multiply" and function_name in tools:
                result = b.Multiply(input)
            elif function_name == "Divide" and function_name in tools:
                result = b.Divide(input)
            else:
                print(f"Unknown functon name: {function_name}")

            updated_input =  f"The result from the previous step is: {result.answer}. Next step: "

        else:
            print(f"Plan output format is incorrect: {step}")
        
        print(f"Result of step {index}: {result.answer}")
    
    return result


if __name__ == "__main__":
    user_input = "Get the sum of ten and twenty and 40, then multiply it by hundred and 200"

    available_functions = [
        {
            "name": "Add",
            "description": "Add two numbers",
        },
        {
            "name": "Subtract",
            "description": "Subtract two numbers",
        },
        {
            "name": "Multiply",
            "description": "Multiply two numbers",
        },
        {
            "name": "Divide",
            "description": "Divide two numbers",
        }
    ]
    tools = [tool["name"] for tool in available_functions]
    plan = generate_plan(user_input=user_input, available_functions=available_functions)
    
    response = execute_plan(plan, tools)
    print(f"Final response: {response.answer}")
