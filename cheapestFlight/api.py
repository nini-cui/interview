import http.client, json

conn = http.client.HTTPSConnection("booking-com15.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "3655499238msh6ea7281926c9923p1f9278jsn2317348cd9e6",
    'x-rapidapi-host': "booking-com15.p.rapidapi.com",
    'Content-Type': "application/json"
}

# conn.request("GET", "/api/v1/flights/searchDestination?query=new", headers=headers)
conn.request("GET", "/api/v1/flights/searchFlights?fromId=MEL.AIRPORT&toId=NKG.AIRPORT&departDate=2026-03-13&adults=1&children=0%2C17&sort=BEST&cabinClass=ECONOMY&currency_code=AUD", headers=headers)

res = conn.getresponse()
resp_data = res.read().decode("utf-8")
resp = json.loads(resp_data)
print(resp)
