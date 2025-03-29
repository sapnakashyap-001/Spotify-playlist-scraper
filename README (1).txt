# Spotify Playlist Scraper

This project scrapes the Billboard Hot 100 songs from a given date and creates a Spotify playlist using the Spotify API.

## Features
- Scrapes song names from Billboard Hot 100 for a given date.
- Searches for songs on Spotify.
- Creates a new Spotify playlist.
- Adds the songs to the playlist automatically.

## Requirements
- Python 3.x
- BeautifulSoup4
- Requests
- Spotipy (Spotify API wrapper)
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sapnakashyap-001/Spotify-playlist-scraper.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Spotify-playlist-scraper
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scriptsctivate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter a date in `YYYY-MM-DD` format to fetch songs from that Billboard Hot 100 chart.

## GitHub Setup (For Uploading Changes)
1. Check the status of your files:
   ```bash
   git status
   ```

2. Add all changes:
   ```bash
   git add .
   ```

3. Commit changes:
   ```bash
   git commit -m "Added Spotify playlist scraper project"
   ```

4. Push changes to GitHub:
   ```bash
   git push origin main
   ```

## License
This project is open-source and available under the MIT License.
