# 音声からアクセントを推定する手法
## ファイルの説明
* [julius](https://github.com/fujielab/fujielab_tools/tree/main/julius-alignment)<br>
fujielab_tools/julius-alignmentの説明に従ってjuliusをインストール．<br>
align_sample/text_kana_basic5000で記号を除去し，align_sampleでエラー処理を実行．<br>
保存先；align_result_01<br>
コピペ先；align_result_5000<br>

* [align_result_5000](./align_result_5000)<br>
Juliusで取得したアライメントを保存．<br>
※形式；Start, End, Mora

* [hubert_2.ipynb](./hubert_2.ipynb)<br>
basic5,000の音声からFAを抽出．<br>
アライメント情報をもとにモーラ単位に分割．<br>
平均プーリングを実行．<br>
保存先；basic5000_jp_HuBERT_features_csv<br>
※形式；Mora，Feature

* [new_directory_transformed](./new_directory_transformed)<br>
align_result_5000のアクセント列を保存．<br>
全部で5000個のファイルを作成し，その中の一列目にAccentというヘッダーを，各行に一個のアクセントを保存．<br>

* [make_F_A.ipynb](./make_F_A.ipynb)<br>
FAの学習データである，rinna_F_Aを作成．<br>
basic5000_jp_HuBERT_features_csvのMora列を削除し、アクセント列を追加．<br>
アクセント列は，basic5000_features_with_accentのアクセント列を別ディレクトリ（new_directory_transformed）に保存したものを使用．<br>
new_directory_transformedには，row_1.csv, row_2.csv, ..., row_5000.csvがあり，中にAccentというヘッダーで各行に一文字ずつ（一列に）0か1が保存されている．<br>
※形式；Accent

* [f0_stac_sample3.py](./f0_stac_sample3.py)<br>
F0の学習データである，fix_f0_stac_result_5000を作成．
BASIC5,000の音声をPyWorldに入力してF0を抽出<br>
アライメント情報をもとにモーラ単位に分割<br>
各モーラ毎のF0の統計値（平均値，最大値，最小値，標準偏差，中央値）を取得<br>
アクセント列を最終列に追加<br>

* [fix_onso_features_accent.ipynb](./fix_onso_features_accent.ipynb)<br>
Mora+特徴量にアクセントを追加．
保存先；basic5000_features_with_accent<br>

## 学習データ
* [rinna_F_A](./rinna_F_A)<br>
make_F_A.ipynbで作成．<br>
HuBERTで抽出し，平均プーリング実行後の特徴量の最終列に，アクセント列（0，1）を追加したデータ．<br>
※形式；Feature_0,..., Feature_767, Accent

* [fix_f0_stac_result_5000](./fix_f0_stac_result_5000)<br>
f0_stac_sample3.pyで作成．<br>
F0の統計値（平均値，最大値，最小値，標準偏差，中央値）の最終列に，アクセント列（0，1）を追加したデータ．<br>
※形式；Mean, Max, Min, Std, Median, Accent


## 実験
* [FA+Transformer](./re5_TransF_FA.ipynb)<br>
FAの学習データを，Transformerの入力に使用．<br>

* [F0+Transformer](./re5_TransF_F0.ipynb)<br>
F0の学習データを，Transformerの入力に使用．<br>

* [FA+LSTM](./re5_LSTM_FA.ipynb)<br>
FAの学習データを，LSTMの入力に使用．<br>

* [F0+LSTM](./re5_LSTM_F0.ipynb)<br>
F0の学習データを，LSTMの入力に使用．<br>
