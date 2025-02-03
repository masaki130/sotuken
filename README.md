# 音声からアクセントを推定する手法
## ファイルの説明
* [julius](https://github.com/fujielab/fujielab_tools/tree/main/julius-alignment)<br>
fujielab_tools/julius-alignmentの説明に従ってjuliusをインストール．<br>
align_sample/text_kana_basic5000で前処理を，align_sampleでエラー処理を実行．<br>
結果は，align_result_5000に保存．<br>

* [align_result_5000](./align_result_5000)<br>
Juliusで取得したアライメントを保存．<br>

* [hubert.ipynb](./hubert.ipynb)<br>
basic5,000の音声からFAを抽出．<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラ毎にFAの平均プーリングを実行．

* [make_F_A.ipynb](./make_F_A.ipynb)<br>
FAの学習データ，rinna_F_Aを作成．
BASIC5,000の音声をHuBERTに入力してF0を抽出<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラ毎に平均プーリングを実行．<br>
アクセント列を最終列に追加<br>

* [f0_stac_sample3.py](./f0_stac_sample3.py)<br>
F0の学習データ，fix_f0_stac_result_5000を作成．
BASIC5,000の音声をPyWorldに入力してF0を抽出<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラ毎のF0の統計値（平均値，最大値，最小値，標準偏差，中央値）を取得<br>
アクセント列を最終列に追加<br>

## 学習データ
* [rinna_F_A](./rinna_F_A)<br>
HuBERTで抽出した特徴量の最終列に，アクセント列を追加したデータ．<br>

* [fix_f0_stac_result_5000](./fix_f0_stac_result_5000)<br>
F0の統計値（平均値，最大値，最小値，標準偏差，中央値）の最終列に，アクセント列を追加したデータ．<br>

## 実験
* [FA+Transformer](./re5_TransF_FA.ipynb)<br>
FAの学習データを，Transformerの入力に使用．<br>

* [F0+Transformer](./re5_TransF_F0.ipynb)<br>
F0の学習データを，Transformerの入力に使用．<br>

* [FA+LSTM](./re5_LSTM_FA.ipynb)<br>
FAの学習データを，LSTMの入力に使用．<br>

* [F0+LSTM](./re5_LSTM_F0.ipynb)<br>
F0の学習データを，LSTMの入力に使用．<br>
