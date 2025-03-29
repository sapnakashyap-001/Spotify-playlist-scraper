import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

date = input("which year do you want to travel to?Type the data in this format YYYY-MM-DD")
url =f"https://www.billboard.com/charts/hot-100/{date}/" 

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=url,headers=header)
spotify_page = response.text

soup = BeautifulSoup(spotify_page,"html.parser")
song_name_spans = soup.select("li ul li h3")
song_name =[song.getText().strip() for song in song_name_spans]


#spotify authenication
sp = spotipy.Spotify( 
        auth_manager = SpotifyOAuth(
        scope= "playlist-modify-private",
        redirect_uri = "http://example.com",
        client_id = os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret =  os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog= True,
        cache_path ="token.txt",
        
        )
)

user_id = sp.current_user()["id"]

print(user_id)




song_URIs =[]
year = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri =result['tracks']["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. skipped ")

        playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
        print(f"playlist created:{playlist['name']}")

        if song_URIs:
           sp.playlist_add_items(playlist_id=playlist["id"], items=song_URIs)
           print("Songs added to the playlist.")
        else:
           print("No songs were found to add.")