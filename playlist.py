import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import argparse

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI', 'http://localhost:8080/callback')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-read-private'))

def get_playlist_tracks(playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = [item['track'] for item in results['items'] if item['track'] is not None]
        return tracks
    except Exception as e:
        print(f"Error fetching tracks for playlist '{playlist_id}': {e}")
        return []

def get_recommendations(seed_tracks, limit=10):
    try:
        recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=limit)
        return [track['id'] for track in recommendations['tracks']]
    except Exception as e:
        print(f"Error fetching recommendations: {e}")
        return []

def print_recommendations(recommendations_ids):
    print("\nRecommended Songs:")
    if recommendations_ids:
        for song_id in recommendations_ids:
            song_name = sp.track(song_id)['name']
            artist_name = sp.track(song_id)['artists'][0]['name']
            print(f"- {song_name} by {artist_name}")
    else:
        print("No recommendations found.")

def main():
    parser = argparse.ArgumentParser(description='Find similar songs based on your playlist.')
    parser.add_argument('playlist_id', type=str, help='The Spotify playlist ID')
    parser.add_argument('--limit', type=int, default=10, help='Number of recommendations to return')
    args = parser.parse_args()

    print(f"\nFetching tracks from playlist ID: {args.playlist_id}...\n")
    tracks = get_playlist_tracks(args.playlist_id)
    
    if not tracks:
        print("No tracks found in this playlist. Please check the playlist ID and try again.")
        return

    seed_tracks = [track['id'] for track in tracks[:5]]
    recommendations_ids = get_recommendations(seed_tracks, limit=args.limit)

    print_recommendations(recommendations_ids)

if __name__ == '__main__':
    main()
