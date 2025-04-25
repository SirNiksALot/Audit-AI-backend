from google import genai
from google.genai import types
from pydantic import BaseModel
import PIL.Image


def assess(image_path) -> str:

    """
    ****Import the following Dependencies****
    from google import genai
    from google.genai import types
    from pydantic import BaseModel
    import PIL.Image
    
    """

    class Date(BaseModel):
        Day: int
        Month: int
        Year: int


    class Product(BaseModel):
        expiry_date: Date
        damaged: bool
        opened:bool

    image = PIL.Image.open(image_path)

    client = genai.Client(api_key="AIzaSyBb5poBl9RArJinjKAxXGe7vg3L6jsBAzo")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Extract the expiry date , if the product is damaged or not , if the product is opened or not in the given format . If Expiry date is not present return 'NA' ", image],
        config={
            'response_mime_type': 'application/json',
            'response_schema': Product,
        }
        )

    return response.text

print(assess("Images\download.jpg"))