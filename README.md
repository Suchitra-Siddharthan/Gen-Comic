# Gen-Comic

An AI-assisted web application that generates educational cybersecurity comics from user-provided security topics. The application uses OpenAI to create a four-panel comic script and renders the output as comic panels through a Flask-based web interface.

---

## Overview

Gen-Comic aims to present cybersecurity concepts in a simple visual format. Users enter a security-related topic such as phishing, malware, ransomware, or firewall, and the application generates a short comic-style story explaining the concept.

The generated comic is accompanied by a brief definition and a security awareness tip.

---

## Features

* Generate 4-panel cybersecurity comics from user input
* AI-generated comic scripts using OpenAI API
* Support for multiple cybersecurity topics
* Automatically generated comic panel images
* Topic definitions displayed alongside comics
* Security awareness tips
* Browser-based text-to-speech for definitions
* Fallback comic generation when API requests fail
* Responsive web interface

---

## Supported Topics

Examples of supported topics include:

* Phishing
* Malware
* Ransomware
* Firewall
* DDoS
* Social Engineering
* Zero-Day Attacks
* IoT Security
* Brute Force Attacks
* Insider Threats
* Supply Chain Attacks
* Cloud Security
* Deepfakes
* Cryptojacking
* Credential Stuffing
* Man-in-the-Middle Attacks
* SIM Swapping
* Scareware
* Botnets
* Biometrics
* Cryptography

---

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* OpenAI API
* Pillow (PIL)
* Requests
* python-dotenv

---

## Project Structure

```text
Gen-Comic/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── bg1.png
│   └── styles.css
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Application Workflow

1. User enters a cybersecurity topic.
2. Flask receives the request.
3. OpenAI generates a four-panel comic script.
4. Panel descriptions are processed and converted into comic panels.
5. A definition for the selected topic is retrieved.
6. The generated comic, definition, and security tip are displayed to the user.

---

## API Endpoints

### Home Page

```http
GET /
```

Renders the main user interface.

---

### Generate Comic

```http
POST /generate
```

#### Request Body

```text
term=phishing
```

#### Response

```json
{
  "term": "phishing",
  "script": "...",
  "definition": "...",
  "panels": [...]
}
```

---

### Security Tip

```http
GET /tip
```

#### Example Response

```json
{
  "tip": "Use strong passwords and enable multi-factor authentication."
}
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Suchitra-Siddharthan/Gen-Comic.git
cd Gen-Comic
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key
```

---

## Running the Application

```bash
python app.py
```

Open the application in a browser:

```text
http://localhost:5000
```

(or the port configured in the application)

---

## Error Handling

The application includes fallback comic scripts for supported topics when OpenAI API requests fail or timeout. This allows comic generation to continue even when external API access is unavailable.

---

## Learning Outcomes

This project demonstrates:

* REST-based web application development using Flask
* Integration of third-party AI APIs
* Prompt-based content generation
* Dynamic image generation with Pillow
* Frontend and backend integration
* Error handling and fallback mechanisms
* Educational content delivery through interactive interfaces


