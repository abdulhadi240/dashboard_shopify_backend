from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/shopify/orders")
async def get_shopify_orders():
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

