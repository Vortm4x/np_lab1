import json

def handle(request_data : bytes) -> dict:
    print(f"Received data: {request_data}")

    try:
        json_request = json.loads(request_data)

        if not isinstance(json_request, dict):
            raise ValueError("JSON data must be a dictionary")

        x_pos : list[int] = json_request['x']
        y_pos : list[int] = json_request['y']
        tile : str = json_request['tile']

        req_dict = {
            'x' : x_pos,
            'y' : y_pos,
            'tile' : tile,
        }

        return req_dict

    except ValueError as e:
        print(f"Error processing JSON data: {e}")
