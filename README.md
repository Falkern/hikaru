# Playlist Recommendation Tool

This project is a Python-based tool that fetches tracks from a specified Spotify playlist and provides song recommendations based on those tracks. It utilizes the Spotify Web API through the `spotipy` library.

## Features

- Fetch tracks from a given Spotify playlist.
- Generate song recommendations based on the fetched tracks.
- Display recommended songs with their names and artists.

## Requirements

- Python 3.6 or higher
- `spotipy` library
- `python-dotenv` library

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Falkern/spotifav.git
   cd spotifav
   ```

2. Install the required libraries:

   ```sh
   pip install spotipy python-dotenv
   ```

3. Create a `.env` file in the root directory and add your Spotify API credentials:
   ```env
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8080/callback'
   ```

## Usage

1. Run the script with the Spotify playlist ID:

   ```sh
   python playlist.py <playlist_id> --limit <number_of_recommendations>
   ```

   Example:

   ```sh
   python playlist.py 37i9dQZF1DXcBWIGoYBM5M --limit 10
   ```

2. The script will fetch tracks from the specified playlist and print out song recommendations.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/) - A lightweight Python library for the Spotify Web API.
- [Spotify for Developers](https://developer.spotify.com/) - Official Spotify Web API documentation.
