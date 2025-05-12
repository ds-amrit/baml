class Steps{
    step string
    function_name string
}

class Functions{
    name string
    description string
}

function GeneratePlan(instructions: string, available_functions: Functions[]) -> Steps[] {
    // This function extracts tasks from meeting notes
    // and returns them as a list of Ticket objects.
    // The implementation is not shown here.
    client "openai/gpt-4o-mini"
    prompt #"
        You are an expert solving problems
        First break down the problem into smaller tasks.
        Assign each task to a function available in the system.
        Do not assign any task to functions that are not available in the system.
    

        {{ctx.output_format}}

        {{_.role("user")}}
        {{instructions}}

        The availble function are:
        {% for tool in available_functions %}
        {{ tool.name }}: {{ tool.description }}
        {% endfor %}

    "#
}

class Answer{
    answer float
}

function Add(input: string) -> Answer {
    client "openai/gpt-4o-mini"
    prompt #"
        You are an expert at mathematics.
        Return the sum of the given numbers.
        {{ctx.output_format}}

        {{_.role("user")}}
        {{input}}
    "#
}

function Subtract(input: string) -> Answer {
    client "openai/gpt-4o-mini"
    prompt #"
        You are an expert at mathematics.
        Return the difference of given numbers
        {{ctx.output_format}}

        {{_.role("user")}}
        {{input}}
    "#
}

function Multiply(input: string) -> Answer {
    client "openai/gpt-4o-mini"
    prompt #"
        You are an expert at mathematics.
        Return the product of given numbers
        {{ctx.output_format}}

        {{_.role("user")}}
        {{input}}
    "#
}

function Divide(input: string) -> Answer {
    client "openai/gpt-4o-mini"
    prompt #"
        You are an expert at mathematics.
        Return the quotient of given numbers
        {{ctx.output_format}}

        {{_.role("user")}}
        {{input}}
    "#
}

test AddTool {
    functions [Add]
    args {
        input #"
            1 + 2
        "#
    }
}
