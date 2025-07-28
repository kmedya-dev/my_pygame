# My Web-Based Adventure Game

This repository contains a simple Python web application featuring a text-based adventure game and a number guessing game.

## Files:
- `main.py`: The Flask web application that serves the game.
- `templates/game.html`: The HTML template for the game's web interface.
- `guessing_game.py`: (Original) A Python script where the computer guesses a number. (Not directly used by the web app anymore).
- `build.sh`: A shell script to install dependencies and run the Flask application.
- `requirements.txt`: Lists the Python dependencies required for the project (e.g., Flask).
- `render.yaml`: Configuration file for deploying the web application to Render.com.
- `.github/workflows/build.yml`: GitHub Actions workflow for continuous integration.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## How to Run Locally:
1.  Ensure you have Python 3 installed.
2.  Navigate to the project directory.
3.  Run the `build.sh` script to install dependencies and start the Flask server:
    ```bash
    ./build.sh
    ```
4.  Open your web browser and navigate to `http://127.0.0.1:5000` (or the IP address shown in the terminal output).

## GitHub Actions:
This project uses GitHub Actions to automatically run the build process on every push to the repository.

## Deployment to Render.com:
This application is configured for deployment to [Render.com](https://render.com) using the `render.yaml` file. You can connect your GitHub repository to Render, and it will automatically build and deploy your web service.