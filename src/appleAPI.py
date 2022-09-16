from calendar import c
import requests
import json


class Apple:
    def extract(self):
        url = "https://amp-api.music.apple.com/v1/catalog/za/playlists/pl.u-AkAmmKpI2bgpVPr/tracks"
        querystring = {"l": "en-gb", }

        payload = ""
        headers = {
            "authority": "amp-api.music.apple.com",
            "authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldlYlBsYXlLaWQifQ.eyJpc3MiOiJBTVBXZWJQbGF5IiwiaWF0IjoxNjYwMzI2MTE4LCJleHAiOjE2NzU4NzgxMTgsInJvb3RfaHR0cHNfb3JpZ2luIjpbImFwcGxlLmNvbSJdfQ.KwV_U4lAWLvOM2z4p2mMZKgb1sQ0vHzf4d7SKKsvtuoVvpZn4bdtjWw_H1ySvTmniU1Rr74QqljRI6k5_AdV0w",
            "cookie": "geo=ZA; dslang=US-EN; site=USA; s_cc=true; mk_epub=^%^7B^%^22btuid^%^22^%^3A^%^221vgh9xx^%^22^%^2C^%^22events^%^22^%^3A^%^22event220^%^3D0.020^%^2Cevent221^%^3D0.030^%^2Cevent222^%^3D0.034^%^2Cevent223^%^3D1.187^%^2Cevent224^%^3D0.468^%^2Cevent225^%^3D0.240^%^2Cevent226^%^3D3.311^%^2Cevent227^%^3D0.030^%^2Cevent228^%^3D1.298^%^2Cevent229^%^3D4.667^%^2C^%^22^%^2C^%^22prop57^%^22^%^3A^%^22www.us.newsroom^%^22^%^7D; s_ppvl=acs^%^253A^%^253Akb^%^253A^%^253Aht^%^253A^%^253Aht203051^%^253A^%^253AHow^%^2520to^%^2520install^%^2520Safari^%^2520extensions^%^2520on^%^2520your^%^2520Mac^%^2520^%^2528en-za^%^2529^%^2C39^%^2C39^%^2C1137.2000122070312^%^2C1536^%^2C726^%^2C1536^%^2C864^%^2C1.25^%^2CP; s_ppv=acs^%^253A^%^253Akb^%^253A^%^253Aht^%^253A^%^253Aht203051^%^253A^%^253AHow^%^2520to^%^2520install^%^2520Safari^%^2520extensions^%^2520on^%^2520your^%^2520Mac^%^2520^%^2528en-za^%^2529^%^2C97^%^2C39^%^2C2847^%^2C1536^%^2C726^%^2C1536^%^2C864^%^2C1.25^%^2CP; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d3c89684d8a3ecf6de211666c62fa40d1ba5d112a6d880f4c62cf7065bbc28efd73367a23b4e29d65189176a418b54d3af11700532f9dd4eb8d1cdb4b8a7cd74584c9d9907b61f3763fe5eebed82730ac67883e2d61d8019ed43635a9b36a26704bcf04fd63f9678d0a2017927c7826ef2986eea96a996209bfd17bda08778c932383c71abe0365116fb3693cc51c87cf8c6254fb4ad95d81df8ee50176f0f2fc1e95ec6066e263594a4af1ecf0b51bd32d55dbbf57bbff3f55c309d81bebbc79f97e9b4aa9791f83f8a5073321f88a24ce7973ff85fc5bc27416bf4f1639e854eb17fee07fcbdc6c5b234043437f0c7ca6aa7bd48e6ead57c430e94965346ce7af913b1f8b01a54b44c48ec54c6f0832d160c5ef2c0fbc6bca1949f1a12005d7d735f3a0fb116a2a78290045773009ce7f393c5b85db1a7b981de1ef9de562cabea79fbca6d9908e8dd4175812a69796e3fffbc32534e3630aab22a9bf055ca3d19bf8b37f9a4ba64b983124b82db9d02d569421fd78e43703eb467bd0ea3194d95783465a61945e794f066d7324dfc520a19f3f6004e235665e243368f540185db88f12e63b7afcb55cc8730aaf0d6e1f9d725f998cdd627f5513dabdfb1cec3ed49841195ea6f05d698a1e92d449ddfd4ce8171a68ef6d56cee16d90204241d3ddef3a72c1b1a4740571094812eb751aaa1216cf8920c8f8fd4ea557e054a7f2c6c639d9ea31bbc15b0da08c939f761d9c82b7ce717cf2651f1917a1344ba9055e0b7c8cadff088b97e9ecc94512c1bacabd2687102af4c4f34ca98e7834de7585a47V3; itspod=36",
            "origin": "https://music.apple.com",
            "referer": "https://music.apple.com/",
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
