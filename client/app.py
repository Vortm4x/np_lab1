import requests
from config import HOST, REVERSE_SORT
import json

def reverse_sort(words : list[str]):
    request_data =  json.dumps({
        'words' : words
    })

    response = requests.post(
        url=f"{HOST}{REVERSE_SORT}",
        json=request_data
    )
    
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data.get('words')
    else:
        error = response_data.get('error')
        raise Exception(error)


def main():

    while True:
        raw_input = input('Unsorted words: ')

        words = raw_input.split(' ')

        try:
            sorted_words = reverse_sort(words)
            print('Reverse-sorted words: ', ' '.join(sorted_words))

        except Exception as e:
            print(e)

        print()


if __name__ == '__main__':
    main()