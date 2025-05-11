class Response{
    question string
    answer string
}

function RAG(question:string, context:string) -> Response {
    // This function performs a retrieval-augmented generation (RAG) task.
    // It retrieves relevant context and generates a response based on the question and context.
    client "openai/gpt-4o-mini"
    prompt #"
        Answer the question in full sentences using the provided context.
        Do not make up an answer. If the information is not provided in the context, say so clearly.
        
        Question: {{question}}
        Context: {{context}}

        {{ctx.output_format}}
        
        {{_.role("user")}}
        {{question}}
        {{context}}
        
        RESPONSE:
    "# 
}

test TestOne {
  functions [RAG]
  args {
    question "When was SpaceX founded?"
    context #"
      SpaceX is an American spacecraft manufacturer and space transportation company founded by Elon Musk in 2002.
    "#
  }
}

test TestTwo {
  functions [RAG]
  args {
    question "Where is Fiji located?"
    context #"
      Fiji is a country in the South Pacific known for its rugged landscapes, palm-lined beaches, and coral reefs with clear lagoons.
    "#
  }
}