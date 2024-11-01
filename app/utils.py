# app/utils.py
import unstructured_client
from unstructured_client.models import operations, shared
from typing import Tuple
import os

# Initialize the Unstructured Client
client = unstructured_client.UnstructuredClient(
    api_key_auth="qm4g9FC8aGBFB0jFxbOSdcUphcXZdT",  # Replace with your actual API key
    server_url="https://api.unstructuredapp.io",
)

def parse_document(file_path: str) -> Tuple[str, dict]:
    # Ensure the file exists before trying to open it
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file was not found: {file_path}")

    print(f"Parsing document at: {file_path}")  # Debug statement

    with open(file_path, "rb") as f:
        data = f.read()

    # Prepare the request
    req = operations.PartitionRequest(
        partition_parameters=shared.PartitionParameters(
            files=shared.Files(
                content=data,
                file_name=os.path.basename(file_path),  # Use just the filename
            ),
            strategy=shared.Strategy.HI_RES,  # Adjust as needed
            languages=['eng'],  # Specify the language
        ),
    )

    # Call the API and handle the response
    try:
        res = client.general.partition(request=req)
        
        # Log the entire response for debugging
        print("API Response:", res)  # Debug statement

        if res.elements:
            # Extract content from each element
            content = "\n".join([element['text'] for element in res.elements if 'text' in element])
            
            # Extract metadata from all elements
            metadata = {}
            for element in res.elements:
                if 'metadata' in element:
                    for key, value in element['metadata'].items():
                        metadata[key] = value  # You may want to adjust how you handle metadata

            return content, metadata
        else:
            raise Exception("No elements returned from the API.")
    except Exception as e:
        raise Exception("Failed to parse document: " + str(e))
