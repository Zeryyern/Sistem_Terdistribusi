from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.post("/soap")
async def soap_endpoint(request: Request):
    # Read raw body (XML)
    body = await request.body()
    print("Incoming SOAP request:")
    print(body.decode("utf-8"))

    # Example SOAP response
    soap_response = """<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <Response>
                <Message>Hello from SOAP API</Message>
            </Response>
        </soap:Body>
    </soap:Envelope>"""

    return Response(content=soap_response, media_type="text/xml")
