import http.client
import json

# Create an HTTP connection
conn = http.client.HTTPConnection("127.0.0.1", 5000)

def printStatus(response):
    print("Status", response.status)
    print("Response:", response.read().decode())


def data_post():
    # Create the data to send in the request body
    data = {
        "username": "Diego",
        "password": "aasadas"
    }

    # Convert the data to JSON format
    json_data = json.dumps(data)

    # Set the headers for the request
    headers = {
        "Content-type": "application/json"
    }

    # Send a POST request with the body
    conn.request("POST", "/players", body=json_data, headers=headers)

    # Get the response
    response = conn.getresponse()
    printStatus(response)

def data_get():

    conn.request('GET', '/players')
    response = conn.getresponse()
    printStatus(response)

def data_getById():
    id = int(input("id:"))
    conn.request('GET', f'/players/{id}')
    response = conn.getresponse()
    printStatus(response)
    

def data_update():
    data = {
        "id":3,
        "username": "Mateo Noel",
        "password": "0001"
    }
    json_data = json.dumps(data)
    headers = {
        "Content-type": "application/json"
    }
    conn.request("PUT", "/players/update", body=json_data, headers=headers)
    response = conn.getresponse()
    printStatus(response)

def data_delete():
    id = int(input("id:"))
    conn.request('DELETE', f"/players/delete/{id}")
    response = conn.getresponse()
    printStatus(response)


data_get()
conn.close()