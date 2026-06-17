from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import io
import time
import textwrap


app = Flask(__name__)
load_dotenv()

import random

def get_random_tip():
    """Return a random cybersecurity tip."""
    tips = [
  "💡 Don't reuse passwords across different sites and apps.",
  "💡 Regularly back up important data to secure locations.",
  "💡 Be cautious of unsolicited calls asking for personal info.",
  "💡 Lock your devices when not in use, even for a moment.",
  "💡 Use antivirus and anti-malware tools to scan regularly.",
  "💡 Review app permissions before installing new software.",
  "💡 Check URLs carefully—look for HTTPS and correct spelling.",
  "💡 Report suspicious emails or activities to your IT/security team.",
  "💡 Disable Bluetooth and Wi-Fi when not actively using them.",
  "💡 Avoid sharing personal details on social media.",
  "💡 Use passphrases instead of simple passwords for better strength.",
  "💡 Don't trust pop-ups claiming your device is infected.",
  "💡 Log out of accounts when using shared or public computers.",
  "💡 Stay updated on the latest cybersecurity threats and scams.",
  "💡 Be wary of QR codes from unknown sources—they can be malicious."
]

    return random.choice(tips)

@app.route('/tip', methods=['GET'])
def get_tip():
    """Return a random cybersecurity tip."""
    return jsonify({"tip": get_random_tip()})


# API Configuration
HF_API_KEY = os.getenv('HF_API_KEY')
OPENAI_KEY = os.getenv('OPENAI_KEY')

def get_term_definition(term):
    """Return definition for security term"""
    definitions = {
  "phishing": "A type of social engineering attack where attackers send fraudulent messages disguised as a reputable source to steal sensitive information.",
  "malware": "Software specifically designed to disrupt, damage, or gain unauthorized access to a computer system.",
  "ransomware": "Malicious software that encrypts a victim's files and demands payment for the decryption key.",
  "firewall": "A security system that filters network traffic to block unauthorized access while permitting legitimate communication.",
  "ddos": "A Distributed Denial-of-Service attack that floods a system with traffic to disrupt services.",
  "social engineering": "Manipulating individuals into divulging confidential information or performing insecure actions.",
  "zero-day": "A previously unknown software vulnerability exploited by attackers before a fix is available.",
  "iot": "Internet of Things devices are connected systems that can be entry points for cyber threats if left unsecured.",
  "brute force": "A trial-and-error method used to decode encrypted data like passwords or PINs by trying all possible combinations.",
  "insider threat": "A security risk originating from within an organization, such as a current or former employee misusing access.",
  "supply chain": "Cyberattacks targeting third-party vendors to compromise a primary organization’s systems.",
  "ai security": "Safeguarding AI systems from manipulation, misuse, and biased or adversarial behavior.",
  "credential stuffing": "An automated attack using stolen credentials to access multiple accounts due to reused passwords.",
  "cloud security": "A set of policies and technologies designed to protect data and applications hosted in the cloud.",
  "deepfake": "AI-generated fake audio or video used to impersonate individuals or falsify events.",
  "cryptojacking": "The unauthorized use of someone’s device to secretly mine cryptocurrency.",
  "man-in-the-middle": "An attack where a malicious actor secretly intercepts and possibly alters communication between two parties.",
  "physical security": "Protection of hardware, networks, and data from physical actions and events that could cause damage or loss.",
  "vishing": "Voice phishing where attackers impersonate legitimate entities over phone calls to extract sensitive data.",
  "typosquatting": "A scam involving fake websites with URLs similar to legitimate ones, designed to deceive users.",
  "watering hole": "A targeted attack where hackers compromise commonly visited websites to infect users within a specific group.",
  "fileless malware": "Malicious code that runs in system memory without leaving files, making it hard to detect.",
  "sim swapping": "A tactic where attackers gain control of a victim’s phone number to intercept messages and access accounts.",
  "scareware": "Deceptive software that frightens users with fake alerts to convince them to install or buy unwanted applications.",
  "botnet": "A network of infected devices controlled remotely by attackers, often used for launching large-scale cyberattacks.",
  "apartment": "Cyber threats originating from nearby physical locations, such as intercepting unsecured Wi-Fi from a neighboring unit.",
  "insider trading": "The illegal practice of trading based on confidential, non-public information from within a company.",
  "whaling": "A phishing scam that targets high-profile individuals like executives, often by impersonating other senior personnel.",
  "shadow it": "Use of unauthorized applications or services by employees without IT approval, potentially exposing the network to risk.",
  "cryptography": "The practice of securing information through encryption, making it unreadable to unauthorized users.",
  "biometrics": "Security mechanisms based on unique physical traits such as fingerprints, facial recognition, or iris scans."
}


    return definitions.get(term.lower(), "No definition available for this term.")

def generate_script(term):
    """Generate a structured comic script with numbered panels"""
    try:
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"""Create a 4-panel comic script about '{term}' in cybersecurity.
Format each panel EXACTLY like this:
1. [Character] [Action/Expression] | [Visual Description]
2. [Character] [Action/Expression] | [Visual Description]
3. [Character] [Action/Expression] | [Visual Description]
4. [Character] [Action/Expression] | [Visual Description]
Include dialogue bubbles where needed. Make it educational but humorous."""

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.8,
                "max_tokens": 500
            },
            timeout=20
        )
        response.raise_for_status()
        script = response.json()['choices'][0]['message']['content']

        # Ensure we get exactly 4 panels
        panels = [line for line in script.split('\n') if line.strip()][:4]
        return panels if len(panels) == 4 else generate_fallback_script(term)

    except Exception as e:
        print(f"Script Error: {e}")
        return generate_fallback_script(term)

def generate_fallback_script(term):
    """Local script generator that varies by term"""
    themes = {
         "phishing": [
            "1. Person receives email: 'You won a prize!' | Show suspicious email on screen",
            "2. Person hovers mouse over link | Magnified view showing fake URL",
            "3. Security guard dog barks at computer | Dog with cyber helmet",
            "4. Person warns friends about phishing | Group looking at secure website"
        ],
        "firewall": [
            "1. Digital wall protecting data castle | Medieval wall with binary code",
            "2. Hackers trying to climb the wall | Cartoon hackers with ladders",
            "3. Firewall guard pushes them away | Guard with 'FW' shield",
            "4. Safe data celebration inside | People dancing with lock icons"
        ],
        "malware": [
            "1. Computer with sick face | Thermometer showing high temp",
            "2. Doctor (antivirus) examining it | Stethoscope on computer",
            "3. Medicine being administered | Shield with 'AV' injecting cure",
            "4. Healthy computer smiling | Green check mark above"
        ],
         "ransomware": [
            "1. Computer crying with chain locks | Files turning into locked vaults",
            "2. Hacker wearing mask holding ransom note | Digital clock counting down",
            "3. IT admin restoring from backup | Cloud-to-computer data transfer",
            "4. Unlocked files celebration | Hackers fleeing with empty bags"
        ],
        "ddos": [
            "1. Army of bot devices firing arrows | Server tower shaking",
            "2. Overloaded server crashing down | '503 Error' signs everywhere",
            "3. Firewall expanding like shield | Blocking attack traffic",
            "4. Normal traffic resuming | Happy users accessing services"
        ],
        "social engineering": [
            "1. Hacker in fake uniform making call | 'IT Support' badge visible",
            "2. Employee handing over credentials | Animated password floating away",
            "3. Security team investigating | Magnifying glass on fake ID",
            "4. Employee shredding fake requests | 'Verify First' poster in background"
        ],
        "zero-day": [
            "1. Sneaky hacker finding software crack | Magnifying glass on code",
            "2. Exploit spreading like virus | Digital contamination animation",
            "3. Developer patching the vulnerability | Sewing needle closing crack",
            "4. Security update notification | Globe-shaped shield forming"
        ],
        "iot": [
            "1. Smart devices with open doors | House network diagram exposed",
            "2. Hacker controlling smart camera | Lens moving suspiciously",
            "3. User changing default passwords | Giant padlock forming",
            "4. Secured smart home | Devices wearing cyber armor"
        ],
        "brute force": [
            "1. Robot trying millions of keys | Keyhole with counter increasing",
            "2. Account lock mechanism engaging | 'Too Many Attempts' sign",
            "3. User creating complex password | Mixing symbols, numbers, letters",
            "4. Hacker's computer exploding | 'Access Denied' in big letters"
        ],
        "insider threat": [
            "1. Employee sneaking data out | USB stick hidden in pocket",
            "2. Data leaking like water drops | Detection system alarm ringing",
            "3. Audit team investigating logs | Paper trail leading to culprit",
            "4. Employee training session | 'Report Suspicious Activity' banner"
        ],
        "supply chain": [
            "1. Infected software update package | Trojan horse in delivery truck",
            "2. Malware spreading through network | Digital spider web pattern",
            "3. Vendor security verification | Checklist with green marks",
            "4. Secured supply chain | Padlocked containers on conveyor belt"
        ],
        "ai security": [
            "1. Rogue AI robot manipulating data | Binary code turning malicious",
            "2. Ethics committee reviewing algorithms | Magnifying glass on code",
            "3. AI bias detection dashboard | Charts showing fairness metrics",
            "4. Secured AI assistant | Robot wearing cyber shield"
        ],
        "credential stuffing": [
            "1. Hacker recycling stolen passwords | Giant password list scrolling",
            "2. Account breached notification | Red alert siren flashing",
            "3. User enabling MFA | Phone approving login attempt",
            "4. Hacker frustrated at MFA prompt | Throwing keyboard"
        ],
        "cloud security": [
            "1. Exposed cloud storage bucket | Open treasure chest in digital sky",
            "2. Hacker climbing cloud infrastructure | Stormy weather approaching",
            "3. Security team encrypting data | Converting files to secure vaults",
            "4. Secured cloud environment | Sunshine over protected data centers"
        ],
        "deepfake": [
            "1. CEO's face morphing on video | Glitch effects around edges",
            "2. Employee transferring funds | Fake authorization document",
            "3. Detection software analyzing pixels | 'Fake' warning label",
            "4. Verification protocol training | Watermark certification process"
        ],
        "cryptojacking": [
            "1. Computer fan overheating | Crypto symbols in exhaust fumes",
            "2. Hidden mining script detected | Pickaxe digging in background",
            "3. Removing malicious code | Cleaning computer with antivirus spray",
            "4. Energy monitor showing normal usage | Green efficiency badge"
        ],
        "man-in-the-middle": [
            "1. Hacker sitting between devices | Copying data packets",
            "2. User seeing fake login page | URL with subtle typos",
            "3. HTTPS padlock forming | Encryption shield activating",
            "4. Hacker's equipment melting | Secure connection established"
        ],
        "physical security": [
            "1. Tailgater entering restricted area | Fake ID badge flashing",
            "2. Security guard checking credentials | Magnifying glass on ID",
            "3. Biometric scanner activating | Facial recognition grid",
            "4. Secure facility celebration | Layers of protection visualized"
        ],
        "vishing": [
            "1. Phone ringing with suspicious number | Caller ID: 'Your Bank'",
            "2. Person revealing OTP | Numbers floating to hacker's notepad",
            "3. Bank fraud department calling | Reverse call tracing animation",
            "4. Phone security workshop | 'Never Share OTP' poster"
        ],
        "typosquatting": [
            "1. User mistyping website URL | 'G00gle.com' instead of Google",
            "2. Fake login page loading | Clone site with subtle differences",
            "3. Password manager autofill refusing | Red X over fake domain",
            "4. Security alert about lookalike sites | Side-by-side comparison"
        ],
        "watering hole": [
            "1. Compromised industry website | Digital poison dripping",
            "2. Employee downloading infected tool | File with hidden malware",
            "3. Network traffic analysis | Detecting unusual connections",
            "4. Sector-wide security alert | Broadcasting to all companies"
        ],
        "fileless malware": [
            "1. Malware hiding in memory | Ghost-like digital creature",
            "2. Legitimate tools being misused | Wrench turning into weapon",
            "3. Memory scanning process | Flashlight revealing hidden code",
            "4. System hardening measures | Locking down PowerShell access"
        ],
        "sim swapping": [
            "1. Fake ID documents at carrier store | Cloned SIM card shining",
            "2. Phone losing signal | 'No Service' notification",
            "3. Two-factor codes being intercepted | SMS bubbles captured",
            "4. Account recovery protections | PIN verification step added"
        ],
        "scareware": [
            "1. Pop-up warning: 'Virus Detected!' | Fake scan results",
            "2. User entering credit card | 'Payment for Protection' form",
            "3. Real antivirus scanning | 'Fake Alert' diagnosis",
            "4. Security awareness training | Recognizing fake alerts"
        ],
        "botnet": [
            "1. Zombie devices waking up | Green cyber veins connecting",
            "2. Massive spam email blast | Envelopes flooding from devices",
            "3. Takedown operation | Authorities unplugging command server",
            "4. Patching vulnerable devices | Software update shields"
        ],
        "apartment": [
            "1. Hacker in nearby apartment | War-driving equipment setup",
            "2. Unsecured WiFi network | Open door with data flowing out",
            "3. VPN encryption activating | Secure tunnel visualization",
            "4. Network security checkup | WiFi analyzer showing strong locks"
        ],
        "insider trading": [
            "1. Employee leaking merger plans | Documents in shadowy envelope",
            "2. Suspicious stock transactions | Charts with abnormal spikes",
            "3. SEC investigators analyzing | Connecting dots on evidence board",
            "4. Compliance training session | 'Report Irregularities' poster"
        ],
        "whaling": [
            "1. Fake CEO email request | 'Urgent Wire Transfer' subject line",
            "2. CFO verifying request | Video call with actual CEO",
            "3. Legal team involved | Contract review with red flags",
            "4. Executive protection training | 'Verify High-Value Requests'"
        ],
        "shadow it": [
            "1. Employee using unauthorized app | Rogue cloud icon",
            "2. Data leaking through gaps | Digital colander metaphor",
            "3. IT discovery process | Radar detecting unauthorized services",
            "4. Approved tools catalog | Employees choosing from secure list"
        ],
        "cryptography": [
            "1. Ancient cipher machine | Transforming into modern locks",
            "2. Quantum computer threatening | Cracking traditional encryption",
            "3. Post-quantum algorithms | New mathematical shields forming",
            "4. Key exchange handshake | Digital keys fitting perfectly"
        ],
        "biometrics": [
            "1. Hacker with facial mask | Failed face recognition attempt",
            "2. Liveness detection activating | 'Blink to Verify' prompt",
            "3. Multi-modal authentication | Face + voice + fingerprint combo",
            "4. Privacy-protected templates | Encrypted biometric data storage"
        ]

    }
    return themes.get(term.lower(), themes["phishing"])

def generate_image(panel_desc):
    """Generate image matching the panel description"""
    try:
        if not HF_API_KEY:
            return create_local_image(panel_desc)

        # Extract visual description after pipe character
        visual_desc = panel_desc.split('|')[-1].strip() if '|' in panel_desc else panel_desc

        response = requests.post(
            "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
            headers={"Authorization": f"Bearer {HF_API_KEY}"},
            json={
                "inputs": f"Cyber security comic panel, {visual_desc}. Clear artwork, bold outlines, vibrant colors",
                "parameters": {"guidance_scale": 9, "num_inference_steps": 30}
            },
            timeout=45
        )
        response.raise_for_status()
        return Image.open(io.BytesIO(response.content))

    except Exception as e:
        print(f"Image Error: {e}")
        return create_local_image(panel_desc)

def create_local_image(panel_desc):
    """Create placeholder image with panel text"""
    img = Image.new('RGB', (512, 512), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    # Try to load font (fallback to default if not found)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # Wrap text and draw centered
    text = panel_desc.split('|')[0] if '|' in panel_desc else panel_desc
    wrapped_text = textwrap.fill(text, width=30)
    draw.multiline_text((50, 50), wrapped_text, fill="black", font=font)

    return img

@app.route('/generate', methods=['POST'])
def generate_comic():
    """Handle comic generation with proper error handling"""
    try:
        term = request.form['term'].strip()
        if not term:
            raise ValueError("Please enter a security term")

        script = generate_script(term)
        definition = get_term_definition(term)
        panels = []

        os.makedirs('static', exist_ok=True)

        # Generate each panel image
        for i, panel_desc in enumerate(script[:4]):
            timestamp = int(time.time())
            panel_path = f"static/panel_{i}_{timestamp}.png"

            img = generate_image(panel_desc)
            img.save(panel_path)
            panels.append({
                "path": panel_path,
                "description": panel_desc
            })

        return jsonify({
            "panels": panels,
            "script": "\n".join(script),
            "term": term,
            "definition": definition,
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",10000))
    app.run(host='0.0.0.0',port=port)