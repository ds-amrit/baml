class WeatherAPI {
  city string
  time string @description("Current time in ISO8601 format")
  temperature string @description("Temperature in Celsius")
}

class CalculatorAPI {
    answer string @description(#" The answer to the calculation.
        The answer should be a string, even if it is a number.
        For example, if the answer is 42, it should be returned as "42".
        Use BODMAS to calculate the answer.
    "#)
}



function SelectTool(message: string) -> WeatherAPI | CalculatorAPI {
  client "openai/gpt-4o"
  prompt #"
    Given a message, extract info.

    {{ ctx.output_format }}

    {{ _.role("user") }} {{ message }}
  "#
}