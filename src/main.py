import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import yaml
from yaml import CLoader as Loader
from urllib.request import urlretrieve


# Initiate Spotify
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path="config/spotipy_cache"))

# Load ad segments
a = urlretrieve("https://raw.githubusercontent.com/simphide/SponsorBlockPodcast/main/ad_segments.yml")[0]
with open(a, 'r') as ad_yaml:
    ad_segments = yaml.load(ad_yaml, Loader=Loader)

# Main loop
while True:
    cp = sp.currently_playing(additional_types="episode")
    if cp is not None and cp["is_playing"]:
        if cp["item"]["id"] in ad_segments:
            for ad_segment in ad_segments[cp["item"]["id"]]:
                if int(ad_segment.split("-")[0]) <= cp["progress_ms"] <= int(ad_segment.split("-")[1]):
                    sp.seek_track(int(ad_segment.split("-")[1]))
    time.sleep(2)


