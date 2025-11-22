## 📌 SaraAssist — Voice-Controlled Desktop Automation Assistant

SaraAssist is a Python-based voice-controlled desktop automation assistant designed to perform multiple computer tasks automatically. It can open applications, search the web, control system settings, manage files, and execute automated workflows using voice commands. The goal is to make daily computer usage faster, hands-free, and more intelligent.

### 🎯 Key Features

- 🎙 Voice command execution (hands-free control)
- ⚙ Open apps & system tools automatically
- 🌍 Perform Google searches via speech
- 📁 File operations & system commands
- ⌨ Automate keyboard/mouse actions
- 🔌 Shutdown / restart / system control
- 🔧 Easy to customize & add new commands

### 🧠 Tech Stack

| Component    | Technology                          |
|-------------|--------------------------------------|
| Language    | Python                               |
| Voice Input | SpeechRecognition, PyAudio           |
| TTS         | pyttsx3 (or similar)                 |
| Automation  | PyAutoGUI, OS, Subprocess           |
| Future AI   | NLP, Intent Classification           |

### 📦 How to Run

```bash
git clone https://github.com/Ashadikram/SaraAssist
cd SaraAssist
pip install -r requirements.txt
python main.py
