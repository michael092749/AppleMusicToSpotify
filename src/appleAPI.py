from calendar import c
import requests
import json


class Apple:
    def extract(self):
        # enter the apple music playslist url here
        url = "https://music.apple.com/za/playlist/africa-now/pl.a0794db8bc6f45888834fa708a674987"
        querystring = {"l": "en-gb", }

        payload = ""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)
        response = response.json()
        # with open("api.json", 'w') as f:
        #     json.dump(response, f)
        return response['data']

    def transform(self, data):
        songs = []
        for index in range(0, len(data)):
            song_name = data[index]['attributes']['name']
            artist = data[index]['attributes']['artistName']
            songs.append(song_name+" "+artist)

        return songs


def main():
    apple_obj = Apple()
    data = apple_obj.extract()
    songs = apple_obj.transform(data)


if __name__ == '__main__':
    main()
