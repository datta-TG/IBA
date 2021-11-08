import os
import openai


def code(text):

    openai.api_key = "KEY"
    prompt="TestStrategy=5\n#Python3\n#context: this dataset is a real estate from Melbourne, it contains information about properties\n#dataset explenation\n#Rooms: Number of rooms\n#Price: Price in dollars\n#Method: S - property sold; SP - property sold prior; PI - property passed in; PN - sold prior not disclosed; SN - sold not disclosed; NB - no bid; VB - vendor bid; W - withdrawn prior to auction; SA - #sold after auction; SS - sold after auction price not disclosed. N/A - price or highest bid not available.\n#Type: br - bedroom(s); h - house,cottage,villa, semi,terrace; u - unit, duplex; t - townhouse; dev site - development site; o res - other residential.\n#SellerG: Real Estate Agent\n#Date: Date sold\n#Distance: Distance from CBD\n#Regionname: General Region (West, North West, North, North east …etc)\n#Propertycount: Number of properties that exist in the suburb.\n#Bedroom2 : Scraped # of Bedrooms (from different source)\n#Bathroom: Number of Bathrooms\n#Car: Number of carspots\n#Landsize: Land Size\n#BuildingArea: Building Size\n#CouncilArea: Governing council for the area\"\"\"\n\n\"\"\" import pandas, streamlit , matplotlib , seaborn, plotly\"\"\"\nimport pandas as pd\n#\n\"\"\" import streamlit\"\"\"\nimport streamlit as st\n#\n\"\"\" import matplotlib\"\"\"\nimport matplotlib.pyplot as plt\n#\n\"\"\" import seaborn\"\"\"\nimport seaborn as sns\n#\n\"\"\" import  plotly\"\"\"\nimport plotly.express as px\n#\n\"\"\"read a dataset call \"data\" using pandas into a variable call \"df\" \"\"\"\ndf = pd.read_csv(\"data.csv\")\n#\n\"\"\"show the propety wiht more Bedrooms\"\"\"\nst.title(\"Property with more bedrooms\")\nst.write(df[df['Bedroom2'] == df['Bedroom2'].max()])\n#\n"

    code=prompt+"\"\"\""+text+"\"\"\""
    response = openai.Completion.create(
    engine="davinci-codex",
    prompt=code,
    temperature=0.1,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0.29,
    presence_penalty=0.2,
    stop=["#"])
    prediction=response['choices'][0]['text']

    return code+prediction
