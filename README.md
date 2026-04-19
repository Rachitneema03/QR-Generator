# QR Generator

A minimal and professional QR Code Generator web app built with Flask and a lightweight frontend.

Users can enter any URL and instantly generate a QR code image. The app includes GitHub action buttons on the UI for starring and contributing to the project.

## Live Project Goals

- Generate QR codes quickly from user-provided URLs
- Keep the interface minimal and clean
- Support easy cloud deployment

## Features

- URL to QR image generation
- Flask backend API endpoint for QR creation
- Frontend served directly by Flask
- CORS support for simple integration scenarios
- Live GitHub star count in the UI
- Contribute button linked to pull requests

## Tech Stack

- Python
- Flask
- qrcode
- Pillow
- Gunicorn (for production)
- HTML, CSS, JavaScript

## Project Structure

QR-CODE/
- backend/
  - main.py
  - requirements.txt
- frontend/
  - index.html
- render.yaml
- README.md

## Local Development

### 1) Clone the repository

git clone https://github.com/Rachitneema03/QR-Generator.git
cd QR-Generator

### 2) Create and activate virtual environment

Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

### 3) Install dependencies

pip install -r backend/requirements.txt

### 4) Run the app

python backend/main.py

### 5) Open in browser

http://127.0.0.1:5000

## API

### POST /generate-qr

Request body (JSON):

{
  "url": "https://example.com"
}

Success response:

{
  "image": "data:image/png;base64,..."
}

Error response:

{
  "error": "URL is required"
}

## Deployment

This repository is deployment-ready for Render.

### Render (Blueprint)

1. Push your latest code to GitHub.
2. In Render, create a new Blueprint.
3. Select this repository.
4. Render detects render.yaml and deploys automatically.

### Render (Manual Web Service)

- Environment: Python
- Root Directory: backend
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn main:app

## Environment

The app uses PORT from environment when deployed.

- Local default: 5000
- Cloud: assigned by hosting provider

## Contributing

Contributions are welcome.

- Open issues for bugs or feature requests
- Submit pull requests for improvements

Contribute directly:
https://github.com/Rachitneema03/QR-Generator/pulls

## License

You can add your preferred license here (for example, MIT).

## Author

Rachit Neema
