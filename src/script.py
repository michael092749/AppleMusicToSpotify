import requests
import json
from appleAPI import Apple


class Spotify:
    def __init__(self) -> None:
        with open("token.json")as keys:
            data = json.load(keys)
            self.ACCESS_TOKEN = data['token']
            self.BASE_URL = data['base_url']
            self.USER_ID = 'users/'+data['client_id']

    def create_Playlist(self, name):
        endpoint = self.BASE_URL+self.USER_ID+'/playlists'

        response = requests.post(
            endpoint,
            headers={
                "Authorization": f"Bearer {self.ACCESS_TOKEN}"
            },
            json={
                "name": name,
                "public": False
            }
        )
        json_response = response.json()
        return json_response['id']

    def add_to_playlist(self, playlist_id, track_id):
        endpoint = self.BASE_URL+'playlists/'+playlist_id+'/tracks'

        response = requests.post(
            endpoint,
            headers={
                "Authorization": f"Bearer {self.ACCESS_TOKEN}"
            },
            json={
                "uris": [track_id]
            }
        )
        json_response = response.json()
        return json_response

    def search_for_track(self, text):
        endpoint = self.BASE_URL+'search'

        response = requests.get(
            endpoint,
            headers={
                "Authorization": f"Bearer {self.ACCESS_TOKEN}"
            },
            params={
                'q': text,

                'type': ['track', 'artist'],
                'limit': 3,
            }
        )
        json_response = response.json()

        with open("response.json", 'w') as f:
            json.dump(json_response, f)

        # with open("response.json", 'r') as f:
        #     out = json.load(f)
        track = json_response['tracks']['items'][0]['uri']

        return track


def main():
    apple_obj = Apple()
    data = apple_obj.extract()
    songs = apple_obj.transform(data)

    spotify_obj = Spotify()
    # track_id = spotify_obj.search_for_track("Pick up the phone")

    playlist = spotify_obj.create_Playlist(name='Kimmy G')
    # print(playlist)
    # playlist = '3sNDt3pXrLB2VemdsaEBBS'
    for song in songs[0:50]:
        print(song)
        track_id = spotify_obj.search_for_track(song)
        x = spotify_obj.add_to_playlist(playlist, track_id)
    print(f"Playlist : {playlist}")


if __name__ == '__main__':
    main()
