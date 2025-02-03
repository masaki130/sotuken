# 音声からアクセントを推定する手法
## ファイルの説明
* [julius](https://github.com/fujielab/fujielab_tools/tree/main/julius-alignment)<br>
fujielab_tools/julius-alignmentの説明に従ってインストール．<br>
align_sample/text_kana_basic5000で前処理を，align_sampleでエラー処理を実行．<br>
結果をalign_result_5000に保存．<br>

* [align_result_5000](./align_result_5000)<br>
Juliusで取得したアライメントを保存．<br>

* [hubert.ipynb](./hubert.ipynb)<br>
basic5,000の音声からFAを抽出．<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラのFAの平均プーリングを実行．

* [FAの学習データ](./align_result_5000)<br>
いいいい
* [F0の学習データ](./f0_stac_sample2.py)<br>
BASIC5,000の音声をPyWorldに入力してF0を抽出<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラのF0の統計値（平均値，最大値，最小値，標準偏差，中央値）を取得<br>
アクセント列を最終列に追加<br>

## 実験
* [FA+Transformer](./re5_TransF_FA.ipynb)<br>
aaa<br>

* [F0+Transformer](./re5_TransF_F0.ipynb)<br>
aaa<br>

* [FA+LSTM](./re5_LSTM_FA.ipynb)<br>
aaa<br>

* [F0+LSTM](./re5_LSTM_F0.ipynb)<br>
aaa<br>
