from baml_client import b
from baml_client.types import PIIExtraction
from typing import Dict, Tuple

def scrub_document(document:str) ->  Tuple[str, Dict[str, str]]:
    """
    Scrub the document of PII and return the scrubbed document and a dictionary of PII found.
    
    Args:
        document (str): The document to be scrubbed.
        
    Returns:
        Tuple[str, Dict[str, str]]: A tuple containing the scrubbed document and a dictionary of PII found.
    """
    # Call the BAML client to extract PII
    pii_extraction = b.ExtractPII(document)
    
    if not pii_extraction.containsSensitivePII:
        # If no PII is found, return the original document and an empty dictionary
        return document, {}
    
    # Create a dictionary to hold the PII found
    scrubbed_document = document
    pii_mapping = {}
    for pii in pii_extraction.privateData:
        pii_type = pii.dataType.upper()
        placeholder = f"[{pii_type}_{pii.index}]"
        pii_mapping[placeholder] = pii.value
        scrubbed_document = scrubbed_document.replace(pii.value, placeholder)

        
    
    
    return scrubbed_document, pii_mapping

def restore_document(scrubbed_document:str, pii_mapping:Dict[str, str]) -> str:
    """
    Restore the document to its original state using the PII mapping.
    
    Args:
        scrubbed_document (str): The scrubbed document.
        pii_mapping (Dict[str, str]): A dictionary of PII found.
        
    Returns:
        str: The restored document.
    """
    restored_document = scrubbed_document
    for placeholder, value in pii_mapping.items():
        restored_document = restored_document.replace(placeholder, value)
    
    return restored_document

# Example usage
document = """
John Smith works at Tech Corp.
You can reach him at john.smith@techcorp.com
or call 555-0123 during business hours.
His employee ID is TC-12345.
"""
# Scrub the document
scrubbed_text, pii_mapping = scrub_document(document)
print("Original Document:")
print(document)
print("\nScrubbed Document:")
print(scrubbed_text)
print("\nPII Mapping:")
for placeholder, original in pii_mapping.items():
    print(f"{placeholder}: {original}")
# If needed, restore the original document
restored_text = restore_document(scrubbed_text, pii_mapping)
print("\nRestored Document:")
print(restored_text)

