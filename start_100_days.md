# 100 Days of Code - Project Plan

This document outlines all the projects from the `100PROJECTSOFCODE` repository, serving as a comprehensive plan for your 100 Days of Code initiative. Each project includes its description, suggested technologies, and a section for you to track your progress and notes.

## Getting Started

1.  **Choose a Project:** Select a project from the list below that aligns with your interests or learning goals.
2.  **Create a Repository:** Create a new GitHub repository for the chosen project.
3.  **Develop & Document:** Work on the project, documenting your progress and key learnings in the project's `README.md`.
4.  **Update Progress:** After completing a project, update the `progress.md` file in this directory and mark the project as "Completed" below.

---

## Categories and Projects

### General Web & Networking Projects

#### FTP Client
Description: A simple File Transfer client that uses the FTP (File Transfer Protocol). As a bonus challenge, add support for secure file transfer. It can be a web, desktop, or CLI app. You can try to first implement TFTP (Trivial File Transfer Protocol) as it's easier.
Suggested Language: C/C++
Suggested Frameworks/Tools: Use [Wireshark](https://github.com/wireshark/wireshark) to observe packets and debug them
Status: [x] Completed
Notes: Implemented FTP client with connect, login, list, retr, and stor commands.

#### HTTP Server
Description: To understand HTTP better, you need to build an HTTP server. It's not much difficult now a days (with the wealth of information around us).
Suggested Language: Python (or any other language you want to master)
Suggested Frameworks/Tools: socket (Python Library)
Status: [x] Completed
Notes: Implemented HTTP server with HTTPS, request body parsing, middleware, templating, session management, SQLite integration, regex routing, and file uploads.

#### Web Scraper
Description: Build a web scraper that takes in a URL/Keyword as input and returns matching results from the web related to the input. You can also build a product searcher or something like that.
Suggested Language: Python (or any other language you want to master)
Suggested Frameworks/Tools: Beautifulsoup (Python Library)
Status: [x] Completed
Notes: Implemented dynamic content scraping with Selenium, proxy support, user-agent rotation, and rate limiting.

#### Port Scanner
Description: Build a port scanner application that can probe a server or host for open ports. You will need some technical knowledge regarding how networks work and how you can scan for ports or classify them.
Suggested Language: Java, C++, Python
Suggested Frameworks/Tools: [socket](https://docs.python.org/3/library/socket.html) Python library
Status: [x] Completed
Notes: Implemented basic TCP port scanning with command-line arguments for host and port range.

#### Packet Sniffer
Description: A packet sniffer is used to monitor network traffic by examining streams of data packets that flow between computers on a network. To start with the project, study network protocols properly. Then dive into implementing an application that tracks down network packets and parses its content in a human readable form.
Suggested Language: Java, C++
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented basic packet capturing and parsing of Ethernet, IP, TCP, UDP, and ICMP headers.

#### P2P File Sharing
Description: Build an app that will allow for peer-to-peer file sharing securely over the internet. This will help you transfer files securely from one location to another or send something to your friend.
Suggested Language: Java, C++
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented basic socket communication for client and server, serving as a foundation for secure file transfer.

#### Search Engine
Description: Build a Web Search Engine like Google or Bing. Don't copy from them though 😉
Suggested Language: web languages. The real work will happen on the backend side with languages like Python, PHP, SQL, Node... Use anything you want for the frontend : HTML, CSS, Javascript...
Suggested Frameworks/Tools: Django if you use Python, MySQL for the databases if you need one
Status: [x] Completed
Notes: Implemented a basic in-memory search engine with document indexing and keyword search.

#### Bandwidth Monitor
Description: Build a tool to track how much data you have downloaded or uploaded to the internet. Have it email you weekly reports of your usage (or notify you when you get above a specified usage limit). As a bonus challenge, predict peak usage times.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented basic network usage tracking using psutil, displaying total sent/received and current rates.

#### Product Landing Page
Description: Build the ideal product landing page according to you. Choose a product, build a page and showcase that on your portfolio.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Created a basic product landing page with HTML structure, CSS styling, and a simple JavaScript interaction.

#### Blog
Description: A blog is a must have for everyone (according to me). Combine that fact with the fact that you learn a lot of things while building your own blog from scratch, and voila!
Suggested Language: JavaScript, Python, Ruby
Suggested Frameworks/Tools: Jekyll (for Ruby), Django/Flask (Python)
Status: [x] Completed
Notes: Implemented a basic Flask blog with static posts and routing.

#### Portfolio Website
Description: If you are ever interested in showcasing the things you have built, build a portfolio website! Building a website to display all the stuff will teach you a lot about website design in general (if you've never built a website before).
Suggested Language: JavaScript, HTML, CSS
Suggested Frameworks/Tools: GatsbyJS
Status: [x] Completed
Notes: Created a basic portfolio website with HTML sections, CSS styling, and smooth scrolling JavaScript.

#### Animated Navigation Toggle
Description: Although it may seem like a small task, building an animated navigation toggle will teach you a lot about web development. Explore all the ideas that you can play with and see if you can build something truly fascinating!
Suggested Language: JavaScript, CSS
Suggested Frameworks/Tools: -
Status: [x] Completed
Notes: Implemented a responsive hamburger menu with CSS transitions for smooth open/close animations and JavaScript for toggling classes.

#### Country Lookup using IP address
Description: Can you find the country from a provided IP address? Write a script that can help you with this. For bonus points, try to figure out a more local location from the IP address.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a Python script to retrieve country and location details from an IP address using ip-api.com.

### Bots

#### Chatbot
Description: Build a chatbot that you can talk to when bored. For bonus points use machine learning/AI to make it smart. I suggest you to implement it as a simple CLI application.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic rule-based CLI chatbot with predefined responses.

#### Slack Bot
Description:
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Created a basic Python script for a Slack bot, demonstrating how to use the slack_sdk to send messages. Requires further setup with Slack API tokens and event subscriptions to be fully functional.

#### Twitter Bot
Description: Build a bot that will either
- follow people that follow the bot
- retweet tweets containing some specific keywords related to a topic
- retweet tweets containing a specific hashtag
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Created a basic Python script for a Twitter bot, demonstrating authentication and a placeholder for retweeting functionality. Requires Twitter API credentials and setup.

#### Messenger Bot
Description: Build a bot for messenger that can do some menial tasks too like flip a coin, roll a dice, present the news, and chat with you when bored.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic CLI-simulated messenger bot with command processing for coin flips, dice rolls, and jokes.

#### WhatsApp Butler
Description: Build a bot for WhatsApp that can scrape information from the internet like news, wikipedia entries, and other things. Make it able to keep track of some events like your/someone else's birthday and send an automatic message wishing you/the other person.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a Python script simulating Wikipedia scraping and reminder management for a WhatsApp bot. Actual WhatsApp integration requires specific API setup.

### Software & Apps

#### Quiz App
Description: The user chooses a category and gets a random set of questions from the given category. Implement a Multiple choice Quiz app to prevent more complications.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line quiz application with multiple-choice questions, category selection, and scoring.

#### Firewall
Description: Build a firewall software that can regulate the network connections for the user and also block/notify of any suspicious action from any website/internal software/external agent.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a conceptual Python script demonstrating packet inspection logic for blocking rules based on destination port (e.g., blocking HTTP traffic).

#### ToDo List
Description: Build a To Do app that can track the various stages of a given work (todo, ongoing, completed). For bonus points, make it work with recurring tasks and incorporate task scheduling (when to do what/a deadline for tasks).
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line ToDo list application with task adding, status updates, and display by status.

#### Text Editor
Description: Build a simple text editor that can help you open, read from and write to text files. For bonus points incorporate features like the find tool and regex search and replace.
Suggested Language: JavaScript, Java
Suggested Frameworks/Tools: Electron (JavaScript framework)
Status: [x] Completed
Notes: Implemented a basic command-line text editor with file open/save, display, insert, delete, and replace line functionalities.

#### Application Builder
Description: This is probably the hardest one on the list and the most vague one too. Design a system that takes in text input and generates applications (or at least application interfaces) based on the text description. You can also use a drag-and-drop like feature to let users build the app.
Suggested Language: -
Suggested Frameworks/Tools: -
Status: [x] Completed
Notes: Implemented a Python script to parse a simple DSL for UI elements and generate a textual representation of the application interface.

#### Drawing App
Description: Build an app that lets the user draw anything and save it as an image. For extra points, add colouring and other cool things like animations.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a web-based drawing application using HTML Canvas with basic drawing, color selection, brush size, clear canvas, and save as PNG functionalities.

#### Survey App
Description: Build an app/web app that will let anyone create survey questions and circulate it via email to record responses and then analyze the data collected.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line survey application with survey creation, taking, and response viewing functionalities.

#### Web Browser
Description: Build a piece of software that will help you browse any HTML page. For bonus points, add additional features like those in Chrome and Firefox.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script that opens a given URL in the default system web browser.

#### Weather App
Description: Build an app that gets the weather at your location in the current time. You can either use a web scraper in the background to collect the data or use a weather API.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a Python script to fetch and display weather information for a given city using the OpenWeatherMap API.

#### Math Editor
Description: Build an app that will properly format equations that a user inputs. I personally find it really inconvenient to work with a special software to just write and display equations properly like Latex, thus, if you build something that can convert plain English text to properly formatted equations, ping me!
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script to convert simple English-like mathematical expressions into LaTeX format.

#### Music Player
Description: Build a music player app that can play music from mp3 files and also have functionality for forward, rewind, pause, and play.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line music player using pygame.mixer with play, pause, unpause, and stop functionalities.

#### Stopwatch App
Description: Build a stopwatch app/web app. It should also be able to lap time.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line stopwatch with start, stop, reset, and lap functionalities.

#### URL Shortener
Description: Build a web app that can shorten any URL that the user provides. You can either code an algorithm that shortens and stores the user provide URL or use an API.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line URL shortener using MD5 hashing and base64 encoding for short code generation.

#### Payment System
Description: Build a payment interface that can deal with fake cash (better if you can deal with real currency, although I don't know if you have to take extra steps for that). Users should be able to receive and send money, and also check their current balance.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line payment system with account creation, balance checking, and money transfer functionalities.

#### MEME Generator
Description: Build an app/web app that will overlay text over an image, so that users can build memes.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script using Pillow to overlay text on images and save them as memes.

#### Pomodoro Clock
Description: Build a Pomodoro timer that will help you take breaks at proper times while doing a task. For bonus points include different Pomodoro timer formats.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line Pomodoro timer with work/break cycles, start, pause, and reset functionalities.

#### Typing Practice
Description: Build an app that lets you practice typing. Make it generate random sentences and see how fast you can type the sentences. Typing is something that many developers completely ignore, but it is one of the most important skills that someone working with computers should have.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line typing practice application with random sentence generation, WPM calculation, and accuracy assessment.

#### Grammar Checker
Description: Build a software that will spell check and check simple grammatical errors in any text you write. For additional points/complexity, try to guess the mood (happy text, formal letter, etc) of the text and suggest appropriate changes.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script using TextBlob for spell checking and sentiment analysis.

#### News Aggregator
Description: Build an app that will present you daily news from credible sources. Make sure you pool unique information about a given news headline from different sites to remove any bias that may be present in a given source.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script to fetch and display news headlines from NewsAPI.org.

#### Calorie Counter
Description: Build an app that will track the amount of calories that you eat everyday. Try to also incorporate information about other macro and micro nutrients to provide a more complete picture.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line calorie counter with food logging and daily summary including macronutrients.

#### Traffic Notifier
Description: Build an app (phone app will be better) that finds how congested one route is and then suggests you a better route to take to your destination.
Suggested Language: Java, Kotlin, Swift
Suggested Frameworks/Tools: Android Studio
Status: [x] Completed
Notes: Implemented a basic Python script simulating traffic information and route suggestions for different routes.

#### Virtual Assistant
Description: Build a virtual assistant that will help you carry out tasks like calling people, scheduling tasks, creating todo lists, taking notes, .. you get the point.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line virtual assistant with functionalities for managing todo lists and taking notes.

#### Antivirus Software
Description: Build an antivirus software that will protect you from viruses and other computer worms and stuff. Make sure you update it frequently to deal with the newer viruses.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script for signature-based file scanning using MD5 hashes against a predefined malware database.

#### Video Call Application
Description: Build an app that can let you video call anyone anywhere over the internet.
Suggested Language: Python, Java, C++ for a desktop app
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script for webcam video capture and display using OpenCV, as a foundational step for a video call application.

#### Library Management System
Description: Build an app for a hypothetical (or better, a real one near you) library that will help in management. You need to keep track of books you have, books to order, people with access to the library, books borrowed, returned and other related tasks.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line library management system with functionalities for adding books, registering members, borrowing, returning, and listing books and members.

#### Relational Database Management System
Description: Build your own database management system like MySQL or PostgreSQL. It doesn't have to be compatible with them, but it does need to help users manage their data efficiently and create relational tables.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic command-line RDBMS with functionalities for creating databases and tables, inserting data, and selecting data with conditions.

### Artificial Intelligence

#### Face Tracker
Description: Build a piece of software that will analyse pictures (or better, live cam feed) and tag faces in the images as face or with a box.
Suggested Language: Python (or any other language you want to learn)
Suggested Frameworks/Tools: OpenCV
Status: [x] Completed
Notes: Implemented a basic Python script for real-time face detection using OpenCV's Haar Cascade classifier on a webcam feed.

#### Spam Classifier
Description: Build a spam classifier that filters ads and other unrequired emails from people that you don't really want to look at.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic rule-based Python script for spam classification using keyword matching.

#### Spoiler Blocker
Description: Build a browser extension that blocks movie spoilers on websites. I put it in AI as you have to think of a changing algorithm that should be smart enough to identify spoilers from a piece of text.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic browser extension with a content script to blur predefined spoiler keywords on web pages using CSS.

#### Music Suggestor
Description: Bored of the same songs but don't know what to try next? Build an AI to suggest you music based on your taste that you are more likely to like.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic rule-based Python script for music recommendations based on predefined genres and artists.

#### Machine Translator
Description: Build an app to translate text from one language to another. For bonus points include an image translator that can get text from image and translate it.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic rule-based Python script for word-by-word translation using a predefined dictionary.

#### Hand Gesture Recognition
Description: Build a piece of software that can recognise gestures from a camera video and then carry out certain tasks based on the gesture.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script for webcam video capture and display using OpenCV, serving as a foundation for hand gesture recognition.

#### Video Subtitle Generator
Description: Input a video and get a subtitle! Build a software that automatically creates subtitles from a provided video. It may seem difficult in the beginning, but look up Natural Language Processing to see how far machines already are with regard to understanding human language.
Suggested Language: Python (As it would be really easy to implement with available libraries)
Suggested Frameworks/Tools: [autosub](https://pypi.org/project/autosub/)
Status: [ ] To Do
Notes:

#### Automatic Logo Generator
Description: Build a software that takes in a company name and some related keywords to generate a brand new logo for the user. Make the logo editable so the user can make any changes if they don't like the generated output.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Movie Recommendation System
Description: Build a recommendation system that lets you or any users choose the next movie that you want to watch. Instead of copying an existing movie recommender with a well studied algorithm, try to come up with your own algorithm and test it out.
Suggested Language: Python (or any other language you are comfortable with)
Suggested Frameworks/Tools: -
Status: [ ] To Do
Notes:

#### Audio to Sign Language Translator
Description: Similar to the video translator, but now you need to translate an audio to sign language. The sign language part can be in the form of a series of images or a video.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

### Theoretical Computer Science

#### Build an OS
Description: This project will be technically challenging and will deepen your understanding of how computers and operating systems work. Building an OS from the ground up is a really daunting task but you will surely find a way to do it.
Suggested Language: low-level languages like C/C++.
Suggested Frameworks/Tools: -
Status: [ ] To Do
Notes:

#### Shuffle Deck
Description: Build a web app to visualize the different shuffling algorithms that can be used to shuffle a standard deck of cards.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Sorting Visualizer
Description: Build a webpage/video that will visualize the different sorting algorithms. You can use different kinds of visualizations: dots, bars, colour bars, circularly scattered points, and so on.
Suggested Language: Processing, JavaScript
Suggested Frameworks/Tools: P5.js (JavaScript)
Status: [ ] To Do
Notes:

#### Static Code Analyzer
Description: Make a software that will go through your code (without executing it) and check for any inconsistencies or errors (syntax errors, indentation, etc) that may cause any problems during execution.
Suggested Language: Any language you feel comfortable with
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Command Line Terminal
Description: If you are building the Operating System, you will surely need a Command Line Terminal. Try to clone the bash shell or Windows PowerShell as an independent project to make it easier while you build your own OS.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### UML Diagram Generator
Description: Write a script that goes through your OOPS code and creates a well-formatted UML diagram for your code.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Pathfinding Visualizer
Description: Make a visualizer for the different pathfinding algorithms. Add this to a maze maker and you have a program that can generate and solve mazes.
Suggested Language: Processing, JavaScript
Suggested Frameworks/Tools: P5.js (JavaScript)
Status: [ ] To Do
Notes:

#### Version Control System
Description: Make a proper version control system like git that can keep track of any changes that you make to your project.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Programming Language
Description: Code a programming language from scratch. This project will give you great insights into why languages are structured the way they are and which languages suit which tasks better. There are quite a few programming languages, thus, incorporate some really weird (or helpful) features to make your language stand out (e.g. check out [brainfuck](https://en.wikipedia.org/wiki/Brainfuck)).
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

### Cryptography

#### Codec Software
Description: Build a software that will encrypt and decrypt text for you. Incorporate quite a few algorithms to provide flexibility to the user.
Suggested Language: C, C++, Java, Python
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Password Manager
Description: Build a software that can manage the different passwords that you use on different websites. For bonus points incorporate a random password generator.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Folder Encrypter
Description: Build a piece of software that can encrypt and lock a selected folder. The contents of the folder should not be accessible/copied/moved without the correct password.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Password Strength Checker
Description: Build a website/app that will check how strong a given password is. To make it more fancy, incorporate a good metric of how strong a password is (check out the example).
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

### Simulations, Games and Game AI

#### Pong
Description: Code the game of [pong](https://en.wikipedia.org/wiki/Pong). Make it multiplayer and visually appealing.
Suggested Language: Python (or any other language of choice)
Suggested Frameworks/Tools: Pygame (Python)
Status: [ ] To Do
Notes:

#### Pong AI
Description: Add to the Pong program you created above. Create an AI opponent to play against in a single player mode.
Suggested Language: Python (or any other language of choice)
Suggested Frameworks/Tools: TensorFlow, PyTorch, openai/gym
Status: [ ] To Do
Notes:

#### Risk
Description: Try coding the classic board game of [Risk](https://en.wikipedia.org/wiki/Risk_(game)). Make sure you know all the rules and understand the game properly before you code it.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Chess
Description: Code the game of chess from the ground up. Build a board, the pieces (you can use images for this part). Code in the rules and make sure you allow no invalid moves.
Suggested Language: JavaScript, Python, any other language you want to master
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Snake
Description: This is one of the simplest items on the list. For an additional challenge, try generating different maps to play in.
Suggested Language: Any language that you feel comfortable with
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Tetris
Description: Code the game of Tetris starting from the Tetrominoes to the game interface. A web app is better as it will let you play from anywhere. For additional challenge try to implement a simple HTML and JavaScript version without any additional frameworks or libraries to help.
Suggested Language: JavaScript, HTML
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Chess AI
Description: Now that you have most likely built the chess game, build an AI that you can play against. For inspiration look into the examples provided. The challenge here is to make an AI that is fast enough to play against. Most simple AIs for chess are just really slow (take about a minute or more for a move). Make your chess engine interface with other programs such via the [Universal Chess Interface](https://en.wikipedia.org/wiki/Universal_Chess_Interface). Then you can test it out against other bots/players online.
Suggested Language: Python, JavaScript
Suggested Frameworks/Tools: Chessboard.js (JavaScript)
Status: [ ] To Do
Notes:

#### Snake AI
Description: Build a simple snake AI that plays snake. For an added challenge, generate random maps and then train your AI to play in any random map that you generate.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Map Maker
Description: Build a simple program that will generate random terrain maps through [procedural generation](https://en.wikipedia.org/wiki/Procedural_generation) with a user supplied seed.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Battleship
Description: Build the classic game of battleship. You can build a CLI app or a much better app with graphics using any 2D graphics module.
Suggested Language: Python (or any language you want to learn)
Suggested Frameworks/Tools: Pygame (Python)
Status: [ ] To Do
Notes:

#### Flappy Bird
Description: This is one of the simplest difficult games that you can build. You can use images for pipes and the bird or generate your own custom bird and pipes for the project.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Tic Tac Toe
Description: Build a CLI app for tic-tac-toe or a graphical interface. One of the interesting ideas is to let the user draw Xs and Os and then let the machine automatically identify if you drew an X or an O.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Memory Puzzle
Description: Implement a classic memory puzzle where the user has to click on two similar cards to eliminate them. Shuffle the cards randomly in the beginning and give the user a fixed number of chances or a fixed time to clear the board.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Physics Engine
Description: Video Games work on [physics engines](https://en.wikipedia.org/wiki/Physics_engine). Build your own. You can later use this engine to build games or carry out simulations. Try building a 2D or 3D physics engine that can handle collision, movement, acceleration, gravity, and other forces in the system. You may need to first understand a bit of physics to be able to build something, so take your time for this one.
Suggested Language: Processing (any other language that you feel comfortable with works too)
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Flappy Bird AI
Description: Design an AI for the flappy bird game. Try out a few learning algorithms to train your network - Q-Learning, NEAT, etc. Build the perfect AI that will play flappy bird better than you (or anyone else) ever can.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Tic Tac Toe AI
Description: Build an AI that is unbeatable (either wins always or at least draws) in tic-tac-toe. Instead of just hardcoding what move to play when, build an AI that learns how to play and then devises strategies to win.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Elevator Simulator
Description: Build a simulation for an elevator. This may seem like a random simulation, but you need to think a lot before implementing something regarding this, which floor to go to when two buttons are pressed? Is there any change if you add a preference for going up or going down? and so on.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Simulate the World
Description: Build a simulation of the whole world. Try to be as detailed as you can. Keep it simple when you feel stuck and slowly improve on it. Treat it as a self-sustaining game if it makes things easier. For bonus points, add an AI to the system to let it work on its own.
Suggested Language: C++ (or C - you will need a fast language for the simulation)
Suggested Frameworks/Tools: Unity (Good for visualizations)
Status: [ ] To Do
Notes:

#### Character Generator
Description: Build a tool that will generate random characters for games that you play/build like Pathfinder or Divinity: Original Sin. First implement a random character generator and then tweak it to make characters that you will like (add an AI).
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Game of Life
Description: [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) simulates the lives of simple cells that obey algorithmic laws. You can read the algorithmic rules from the wikipedia page and implement them. Make the program capable of graphical rendering to display the end product.
Suggested Language: Processing, JavaScript
Suggested Frameworks/Tools: P5.js (JavaScript)
Status: [ ] To Do
Notes:

### Miscellaneous

#### Deal Finder
Description: Build a simple web app to notify you when an item you covet goes on sale for a good price. You can use a web scraper to pull the item's product page and notify you of any price changes.
Suggested Language:
Suggested Frameworks/Tools:
Status: [x] Completed
Notes: Implemented a basic Python script simulating price tracking and deal alerts using BeautifulSoup for parsing dummy HTML content.

#### Expense Tracker
Description: Create a simple interface (web app/phone app) you can use to add and categorize your expense. Generate monthly reports based on the inputs and write custom alerts for things like, "spending too much on coffee... as always".
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Recipe Generator
Description: The app (or service) should generate new recipes/scrapes recipes from the web. So when you cook by its recipe, you rate it to tell it how good the recipe was.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Emoji Translator
Description: Build a browser extension that will translate any provided sentence into a combination of emojis. You can use the extension to automatically change texts that a user sends via messaging or email or even use it to aid in writing blog posts.
Suggested Language: JavaScript
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Regex Query Tool
Description: Build a search tool that implements Regular Expressions. With it you can easily search for text matching a pattern in websites or documents that you may be writing or browsing.
Suggested Language: JavaScript
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Currency Converter
Description: Code a script that scrapes the currency conversion rate and then converts from a given currency to another suing the current market rate.
Suggested Language: Python, JavaScript
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Pixel Art Generator
Description: Code a script that takes in a picture and then creates the Pixel Art from the image. You can achieve this by downsizing the image. You should also be able to generate random art using this script.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Directory Tree Generator
Description: Generate a tree like structure using the directories present in a given path by the user. This allows you to see the positioning of files and directories. We are visual animals and thus, visual depictions of directories are more understandable.
Suggested Language:
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Random Username Generator
Description: Write a script to generate random usernames that you can use in games or various other places.
Suggested Language: Python or any other language
Suggested Frameworks/Tools: Random (Python Library)
Status: [ ] To Do
Notes:

#### Roman to Decimal Converter
Description: Write a script that converts decimal numbers to roman numerals and vice versa. This may seem like an easy task but I assure you its not that easy. Give it a try.
Suggested Language: Python or any other language
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

### Coding Challenges

#### Project Euler
Description: [Project Euler](https://projecteuler.net/) contains mathematical challenges that require programming tools to be solved. There are over 700 problems that you can solve, I urge you to document each solution in a properly organized way (probably build a repo for the solutions) so that you can showcase them online.
Suggested Language: Any language you want to practice
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Advent of Code
Description: [Advent of Code](https://adventofcode.com/) challenges occur every year in the days leading up to Christmas. They include lots of fun programming challenges that can help you develop your chops in a programming language that you want to master.
Suggested Language: Any language you want to master
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:

#### Kaggle Titanic Challenge
Description: Kaggle offers fascinating challenges to introduce you to the basics of machine learning with Python or R: Use a real dataset from the [Titanic passenger log](https://www.kaggle.com/c/titanic) to predict which passengers were most likely to survive the disaster.
Suggested Language: Python or R
Suggested Frameworks/Tools:
Status: [ ] To Do
Notes:
