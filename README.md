# VOICEVOX Text-to-Speech Web App with Streamlit

This project is a **Streamlit-based web application** that synthesizes speech from Japanese text entered on a web page using the [VOICEVOX](https://voicevox.hiroshiba.jp/) engine locally.
(Note: The app will not work as-is without the `voicevox` folder. Installation instructions are provided below.)

## ✨ Features

* Easy voice synthesis via browser using the Streamlit Web UI
* Automatic launching of the VOICEVOX engine (`run.exe` supported)
* Includes speaker selection, audio playback, and download features

---

## ⚡ How to Run Demo (Windows)

### ▶ 1. Clone the Repository

```bash
git clone https://github.com/ty70/voice-text-to-speech.git
cd voice-text-to-speech
```

### ▶ 2. Install the VOICEVOX Engine

Refer to [Step 2 from this guide](https://github.com/ty70/voicevox-text-to-speech.git) for instructions on installing VOICEVOX.
Rename the resulting folder to `voicevox` and place it in the root directory.

### ▶ 3. Install Required Packages

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install streamlit requests
```

### ▶ 4. Launch the Streamlit App (VOICEVOX launches automatically)

```bash
streamlit run app.py
```

On first launch, the VOICEVOX engine will start in the background. Once initialized, the app will be accessible via a web interface.

---

## 🌐 App Features

* Text Input: Any Japanese text
* Speaker Selection: Includes options such as Shikoku Metan, Zundamon, Ryusei Aoyama (via speaker IDs)
* Audio Generation: Utilizes the VOICEVOX API
* Playback & Download: Provided in WAV format

---

## 🛠 Project Structure

```
.
├─ voicevox/         # Folder for placing run.exe (must be prepared separately)
├─ app.py            # Main Streamlit app (includes VOICEVOX launch)
├─ LICENSE
├─ README_ja.md      
├─ README.md         # This file
├─ requirements.txt  # Required Python packages
└─ utils.py          # Functions for speech generation
```

---

## 📅 TODO / Future Enhancements

* Speed and pitch adjustment
* Batch generation for multiple speakers
* Input history saving
* Docker / Linux support

---

## ✅ LICENSE

This project is provided under the [MIT License](./LICENSE).
Please follow the VOICEVOX official license and terms of use when using the VOICEVOX engine.

---

## 🙏 Special Thanks

* The VOICEVOX Development Team
* [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)
* [Hiroshiba](https://github.com/hiroshiba)
