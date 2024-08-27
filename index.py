from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(
    title="Shopify API",
    description="API to interact with Shopify",
    version="1.0.0",
    servers=[
        {
            "url": "https://dashboard-shopify-backend2.onrender.com",
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

@app.get("/orders", response_description="The URL to fetch orders from Shopify")
async def get_shopify_orders():
    """Fetches and returns Shopify orders from the specified URL.
    This endpoint makes a fetch call to the URL and retrieves orders from Shopify, which are then converted to JSON and returned."""
    url = "https://dashboard-shopify-backend.onrender.com/shopify/orders"
    headers = {
        "X-Shopify-Access-Token": "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"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Raises an exception for 4XX/5XX responses
            return response.json()  # Return the JSON response from Shopify
        except httpx.HTTPStatusError as http_err:
            raise HTTPException(status_code=response.status_code, detail=str(http_err))
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
