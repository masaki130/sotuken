# 音声からアクセントを推定する手法
## ファイルの説明
* [julius](https://github.com/fujielab/fujielab_tools/tree/main/julius-alignment)<br>
fujielab_tools/julius-alignmentの説明に従ってインストール．<br>
align_sample/text_kana_basic5000で前処理を，align_sampleでエラー処理をした．<br>
結果をalign_result_5000に保存．

* [align_result_5000](./align_result_5000)<br>
Juliusで取得したデータにモーラ列を追加．<br>

* [FAの抽出](./align_result_5000)<br>
いいいい
* [FAの学習データ](./align_result_5000)<br>
いいいい
* [F0の学習データ](./f0_stac_sample2.py)<br>
BASIC5,000の音声をPyWorldに入力してF0を抽出<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラのF0の統計値（平均値，最大値，最小値，標準偏差，中央値）を取得<br>
アクセント列を最終列に追加<br>
