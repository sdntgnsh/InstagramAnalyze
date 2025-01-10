# Instagram Analyzer

## Description

The Instagram Analyzer is a project that analyzes your Instagram account and provides insights based on your posts, engagement, and audience. This project uses natural language processing and machine learning algorithms to provide personalized answers to questions provided by the user.

## Screenshots

![Screenshot 1](https://github.com/sdntgnsh/InstagramAnalyze/screenshots/s1.png?raw=true)
![Screenshot 2](https://github.com/sdntgnsh/InstagramAnalyze/screenshots/s2.jpg?raw=true)
![Screenshot 3](https://github.com/sdntgnsh/InstagramAnalyze/screenshots/s3.jpg?raw=true)

## Features

* Analyzes Instagram posts and comments to provide insights on engagement, audience, and content performance
* Uses natural language processing to understand user questions and provide relevant answers
* Provides personalized recommendations for improving Instagram content and engagement

## Technical Details

* Built using:
  * **LangFlow**: for natural language processing and machine learning
  * **Flask**: for building the backend API
  * **React**: for building the frontend user interface
  * **Instaloader**: for collecting Instagram data
  * **AstraDB**: for storing and querying data
* Deployed on: [render.com](https://www.render.com)

## How it Works

1. User connects their Instagram account to the analyzer
2. Analyzer collects data on user's Instagram posts, comments, and engagement using Instaloader
3. Data is stored in AstraDB for querying and analysis
4. User asks a question about their Instagram account (e.g. "What type of content gets the most engagement?")
5. LangFlow uses natural language processing to understand the question and provide a relevant answer based on the collected data
6. Answer is displayed to the user through the React frontend

## Example Use Cases

* "What type of content gets the most engagement on my Instagram account?"
* "Who are my most engaged followers?"
* "What are the most common hashtags used in my posts?"

### Prerequisites

* Python 3.8+
* Node.js 14+
* npm 6+
* AstraDB instance (see [AstraDB documentation](https://docs.astradb.com/) for setup instructions)
* Instagram API credentials (see [Instagram API documentation](https://developers.facebook.com/docs/instagram-api/) for setup instructions)

### Setup

1. Clone the repository: `git clone https://github.com/[your-username]/[your-repo-name].git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `npm install` and `pip install -r requirements.txt`
5. Set up AstraDB instance and create a database for the project
6. Set up Instagram API credentials and create a file `instagram_credentials.json` with the following format:

    ```json
    {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "access_token": "your_access_token"
    }
    ```

7. Set up your AstraDB credentials in the `config.py` file
8. Run the backend: `python app.py`
9. Run the frontend: `npm run dev`

## Contributing

We welcome contributions to this project! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT license. See the LICENSE file for details.
