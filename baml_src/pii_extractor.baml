class PIIData {
  index int
  dataType string
  value string
}

class PIIExtraction {
  privateData PIIData[]
  containsSensitivePII bool @description("E.g. if the document contains sensitive PII data make it true else false")
}

function ExtractPII(document: string) -> PIIExtraction{
    client "openai/gpt-4o-mini"
    prompt #"
        Extract all personally identifiable information (PII) from the given document. Look for items like:
    - Names
    - Email addresses
    - Phone numbers
    - Addresses
    - Social security numbers
    - Dates of birth
    - Any other personal data

    {{ctx.output_format}}

    {{_.role("user")}}
    The given document is: \n
    {{document}}
    "#
}

test PIIExtraction {
    functions [ExtractPII]
    args{
        document #"
        John Doe, born on 01/01/1990, lives at 123 Main St, Springfield, IL. His email is john_doe@gmail.com
        and his phone number is (555) 123-4567. He has a social security number of 123-45-6789.
        Jane Smith, born on 02/02/1985.
        Her email is jane@smith
        She is a software engineer at Tech Corp.
        "#
    }
}

test EmptyDocument {
  functions [ExtractPII]
  args {
    document "This document contains no PII data."
  }
}