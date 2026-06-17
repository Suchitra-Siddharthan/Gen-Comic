# CyberSnaps – AI-Powered Security Comic Generator

## Overview
**CyberSnaps** is an AI-based comic generator that transforms dry cybersecurity topics into engaging 4-panel comics using humor and storytelling.  
Designed to simplify complex security concepts like phishing, DDoS, and malware, the platform offers an interactive way to educate users through visually appealing and relatable content.

## Problem Statement
Cybersecurity awareness is essential in today's digital landscape, yet most people overlook traditional security training because it tends to be text-heavy and unengaging.  
This leads to recurring issues like phishing attacks, password leaks, and social engineering exploits.  
There is a growing need for an educational tool that is not only informative but also fun and interactive.

## Solution
CyberSnaps addresses this problem by allowing users to input a cybersecurity topic and receive a comic strip that explains the concept in a humorous, easy-to-understand format.  
The generated comics are ideal for awareness campaigns, employee training, and social media education.

## Key Features
- Input a security term (e.g., phishing, malware, DDoS)
- AI-generated 4-panel comic strip
- Uses storytelling, humor, and characters
- Simple UI for seamless interaction
- Read Definition button using Web Speech API to read it aloud
- Automatically fetches a random cybersecurity tip on every page load
- Gets feedback from the user


## Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python (Flask)        |
| AI (Text)   | OpenAI GPT-3.5-turbo  |
| AI (Image)  | Hugging Face APIs     |

## Implementation Details
1. User inputs a topic on the user interface  
2. The system generates a custom prompt for the AI model  
3. GPT-3.5-turbo generates a 4-caption comic script  
4. Hugging Face APIs generate visuals based on the script  
5. Comic panels are rendered dynamically in a 4-panel layout  
6. Final comic is displayed on screen with an option to share or download
7. Reads Definition using Web Speech API 
 

## Team Members
- Oviyashree C J  
- Roopa Varshni R  
- Suchitra S  
