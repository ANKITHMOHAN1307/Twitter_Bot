<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Twitter Bot Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        h1 {
            font-size: 2em;
        }
        section {
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
            font-size: 1.5em;
        }
        code {
            background-color: #f1f1f1;
            padding: 5px;
            border-radius: 5px;
        }
        ul {
            list-style-type: square;
            margin-left: 20px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Twitter Bot Project</h1>
</header>

<section>
    <h2>🚀 Features</h2>
    <ul>
        <li><strong>Automated Tweeting:</strong> Tweets based on current trending topics.</li>
        <li><strong>Scheduled Tweets:</strong> Tweets automatically posted at midnight every day.</li>
        <li><strong>Easy Setup:</strong> Simple steps to configure the bot with your Twitter credentials.</li>
    </ul>
</section>

<section>
    <h2>🛠️ Installation</h2>
    <p>Follow these steps to set up the Twitter Bot on your local machine:</p>
    <ul>
        <li>Clone this repository to your local machine:
            <br><code>git clone https://github.com/yourusername/twitter-bot.git</code>
        </li>
        <li>Navigate to the project directory:
            <br><code>cd twitter-bot</code>
        </li>
        <li>Install required dependencies:
            <br><code>pip install -r requirements.txt</code>
        </li>
    </ul>
</section>

<section>
    <h2>⚙️ Configuration</h2>
    <p>Create a <code>.env</code> file in the root of the project with your Twitter credentials:</p>
    <pre>
    CONSUMER_KEY=your_consumer_key
    CONSUMER_SECRET=your_consumer_secret
    ACCESS_TOKEN=your_access_token
    ACCESS_SECRET=your_access_secret
    </pre>
</section>

<section>
    <h2>🏃‍♂️ How to Run</h2>
    <p>To run the bot, simply execute:</p>
    <pre><code>python bot.py</code></pre>
    <p>Your bot will start and tweet automatically at midnight each day!</p>
</section>

<section>
    <h2>🔧 Dependencies</h2>
    <p>The following libraries are required to run the Twitter Bot:</p>
    <ul>
        <li><strong>Tweepy:</strong> Python library for interacting with the Twitter API.</li>
        <li><strong>Schedule:</strong> Library for scheduling tasks.</li>
    </ul>
</section>

<section>
    <h2>📋 License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>
</section>

<footer>
    <p>Made with ❤️ by <strong> Ankith MOhan </strong></p>
</footer>

</body>
</html>
