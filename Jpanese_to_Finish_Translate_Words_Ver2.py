# Google ColabでGoogle Driveをマウント
from google.colab import drive
drive.mount('/content/drive')

# gTTS（Google Text-to-Speech）ライブラリをインストール
!pip install gTTS

# gTTSを使用してテキストを音声に変換
from gtts import gTTS
import os

# Google Drive内のテキストファイルのパスを指定
text_file_path = '/content/drive/MyDrive/fin_Scraping/Translate_JP/translated_output_5.txt'

# 出力ディレクトリを指定
output_directory = '/content/drive/MyDrive/finrand/finland_13'

# 出力ディレクトリが存在しない場合、作成
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# テキストファイルからフィンランド語を検出し、音声ファイルを生成
with open(text_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    # カンマで分割してフィンランド語と日本語の部分を取得
    parts = line.strip().split(',')

    if len(parts) >= 2:
        japanese_text = parts[0].strip()  # カンマの1番目の文字をファイル名として取得
        finnish_text = parts[1].strip()  # カンマの2番目の文字をフィンランド語として取得
        # ファイル名から/を取り除く
        japanese_text = parts[0].strip().replace('/', '_')  # スラッシュをアンダースコアに置き換える
        # フィンランド語のテキストを音声に変換
        tts = gTTS(text=finnish_text, lang='fi')
        # 音声ファイルを指定の場所に保存
        output_path = os.path.join(output_directory, f'{japanese_text}.mp3')
        tts.save(output_path)
print("音声ファイルの作成が完了しました。")
