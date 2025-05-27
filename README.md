# VOICEVOX Text-to-Speech Web App with Streamlit

このプロジェクトは、[VOICEVOX](https://voicevox.hiroshiba.jp/) エンジンを利用して日本語テキストから音声を合成する **StreamlitベースのWebアプリケーション** です。
（voicevoxフォルダがないので、動きません、voicevoxの導入方法は、[ここから](https://github.com/ty70/voicevox-text-to-speech.git), 出来たフォルダをvoicevoxにリネームして使って下さい。

## ✨ 特徴

* Streamlit Web UI により、簡単にブラウザ上で音声合成が可能
* VOICEVOXエンジンの自動起動（`run.exe`）に対応
* 話者の選択、音声再生、ダウンロード機能を搭載

---

## ⚡デモ実行方法（Windows）

### ▶ 1. リポジトリのクローン

```bash
git clone https://github.com/ty70/voice-text-to-speech.git
cd voice-text-to-speech
```

### ▶ 2. VOICEVOXエンジンの配置

VOICEVOXエンジンのWindows用実行ファイルをダウンロードし、`voicevox/` フォルダ内に `run.exe` を配置してください。

* ダウンロード: [https://github.com/VOICEVOX/voicevox\_engine/releases](https://github.com/VOICEVOX/voicevox_engine/releases)

### ▶ 3. 必要パッケージのインストール

```bash
pip install -r requirements.txt
```

または：

```bash
pip install streamlit requests
```

### ▶ 4. Streamlit アプリ起動（VOICEVOXも同時起動）

```bash
streamlit run app.py
```

初回起動時に VOICEVOX エンジンがバックグラウンドで起動されます。正常に起動するとWebページ上で操作可能になります。

---

## 🌐 アプリ機能

* 文本入力: 任意の日本語テキスト
* 話者選択: 四国めたん、ずんだもん、青山龍星など（speaker ID使用）
* 音声生成: VOICEVOX APIを使用
* 再生・ダウンロード: WAV形式で提供

---

## 🛠 構成

```
.
├─ voicevox/         # run.exeを配置するフォルダ
├─ app.py            # Streamlitアプリ本体（VOICEVOX起動含む）
├─ LICENSE
├─ README.md         # このファイル
├─ requirements.txt  # 必要パッケージ
└─ utils.py          # 音声生成関数
```
---

## 📅 TODO / 拡張案

* 速度・ピッチ調整
* 複数話者一括生成
* 入力履歴の保存
* Docker対応 / Linux対応版

---

## ✅ LICENSE

このプロジェクトは [MIT ライセンス](./LICENSE)で提供されます。
VOICEVOXエンジンの使用については、VOICEVOX公式のライセンス・利用規約に従ってください。

---

## 🙏 Special Thanks

* VOICEVOX開発チーム
* [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)
* [Hiroshiba氏](https://github.com/hiroshiba)
