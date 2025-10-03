import requests

# The server URL (adjust port if needed)
url = "http://127.0.0.1:8000/soap"

# Example SOAP request XML
soap_request = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetMessage>
            <Name>Zayyanu</Name>
        </GetMessage>
    </soap:Body>
</soap:Envelope>"""

# Send the request
headers = {"Content-Type": "text/xml; charset=utf-8"}
response = requests.post(url, data=soap_request, headers=headers)

# Print server response
print("Status:", response.status_code)
print("Response XML:")
print(response.text)
