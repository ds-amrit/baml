enum UserMessage{
    SPAM
    NOT_SPAM
}

function ClassifyText(text: string) -> UserMessage {
    client "openai/gpt-4o-mini"
    prompt #"
        classify the following message:
            
        
        {{ctx.output_format}}

        {{_.role("user")}}
        text: {{text}}
        
    "#
}

test BasicSpamTest {
    functions [ClassifyText]
    args {
        text "Congratulations! You've won a $1000 gift card. Click here to claim your prize."
    }
}

test BasicNotSpamTest {
    functions [ClassifyText]
    args {
        text "Hey, do you want to grab lunch tomorrow?"
    }
}

enum TicketLabel {
  ACCOUNT
  BILLING
  GENERAL_QUERY
}
class TicketClassification {
  labels TicketLabel[]
}

function ClassifyTicket(ticket: string) -> TicketClassification {
  client "openai/gpt-4o-mini"
  prompt #"
    You are a support agent at a tech company. Analyze the support ticket and select all applicable labels.
    {{ ctx.output_format }}
    {{ _.role("user") }}
    
    {{ ticket }}
  "#
}

test ClassifyTicketSingleLabel {
  functions [ClassifyTicket]
  args {
    ticket "I want to increase my salary"
  }
}
test ClassifyTicketMultiLabel {
  functions [ClassifyTicket]
  args {
    ticket "My account is locked and I can't access my billing information"
  }
}

