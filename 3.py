import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog, Text, Scrollbar

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language='ja-JP')
        return text
    except sr.UnknownValueError:
        print("音声を認識できませんでした")
        return None
    except sr.RequestError as e:
        print(f"Google Web Speech API エラー: {e}")
        return None

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)

def convert_and_display():
    audio_file_path = entry.get()
    result = audio_to_text(audio_file_path)
    
    if result:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)

# GUIアプリケーションの作成
app = tk.Tk()
app.title("音声認識アプリ")

# ファイル選択ボタン
file_select_button = tk.Button(app, text="ファイル選択", command=open_file_dialog)
file_select_button.pack(pady=10)

# 入力ファイルパスのエントリー
label = tk.Label(app, text="音声ファイルパス:")
label.pack(pady=5)

entry = tk.Entry(app, width=40)
entry.pack(pady=5)

# 変換ボタン
convert_button = tk.Button(app, text="変換", command=convert_and_display)
convert_button.pack(pady=10)

# 出力テキストウィジェット
output_text = Text(app, height=10, width=50, wrap=tk.WORD)
output_text.pack(pady=10)

# スクロールバー
scrollbar = Scrollbar(app, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)

# アプリケーションの実行
app.mainloop()
