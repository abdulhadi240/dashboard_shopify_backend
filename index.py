from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Shopify API",
    description="API to interact with Shopify",
    version="1.0.0",
    servers=[
        {
            "url": "https://dashboard-shopify-backend.onrender.com",
            "description": "Shopify API"
        }
        
    ]
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/shopify/orders",response_description="The URL to fetch orders from shopify")
async def get_shopify_orders():
    """Fetches and return shopify order from the specifeid URL
    This endpoint make a fetch call to the url and get the orders from the shopify which is then converted to json and return as a json"""
    url = "https://b519f5-ff.myshopify.com/admin/api/2024-07/orders.json"
    headers = {
        "X-Shopify-Access-Token": "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",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception for 4XX/5XX responses
        return response.json()  # Return the JSON response from Shopify
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

