import streamlit as st
from utils import synthesize_voice
import subprocess
import time
import os
import requests
import atexit

VOICEVOX_PATH = "./voicevox/run"
VOICEVOX_URL = "http://127.0.0.1:50021"

# グローバル変数としてプロセスを保持
voicevox_process = None

@st.cache_resource(show_spinner="VOICEVOXエンジンを起動しています…")
def start_voicevox():
    global voicevox_process
    if not os.path.exists(VOICEVOX_PATH):
        st.error(f"VOICEVOXエンジンが見つかりません: {VOICEVOX_PATH}")
        return None
    # run.exe を起動
    voicevox_process = subprocess.Popen([VOICEVOX_PATH, "--host", "127.0.0.1", "--port", "50021"])
    # 起動待ち
    for _ in range(20):
        try:
            requests.get(VOICEVOX_URL)
            return voicevox_process
        except:
            time.sleep(0.5)
    st.error("VOICEVOXエンジンの起動に失敗しました ❌")
    return None

# アプリ終了時にVOICEVOXを終了する
def cleanup():
    global voicevox_process
    if voicevox_process and voicevox_process.poll() is None:
        voicevox_process.terminate()
        voicevox_process.wait()
        print("VOICEVOXエンジンを終了しました。")

atexit.register(cleanup)

# VOICEVOXを起動
start_voicevox()

# アプリ本体UI
st.title("🎤 VOICEVOX テキスト読み上げアプリ")
text = st.text_area("📄 読み上げるテキスト", "こんにちは、ストリームリットから話しています。")
speaker_id = st.selectbox("🔊 話者", [1, 3, 14], format_func=lambda x: {1: "四国めたん", 3: "ずんだもん", 14: "青山龍星"}.get(x, str(x)))

if st.button("▶️ 音声生成"):
    if text.strip():
        output_path = synthesize_voice(text, speaker_id)
        if output_path:
            audio = open(output_path, 'rb').read()
            st.audio(audio, format="audio/wav")
            st.download_button("💾 音声をダウンロード", audio, file_name="voice.wav")
        else:
            st.error("音声生成に失敗しました")
    else:
        st.warning("テキストを入力してください")