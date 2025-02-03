# 低；0、高；1
# 特徴量とアクセントを統合したデータ
# fix_f0_stac_result_5000に保存
# 各音節における統計値とaccentを保存
# 実行：python f0_stac_sample3.py --num_files 3
from __future__ import division, print_function
import os
from shutil import rmtree
import argparse
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pyworld as pw
import scipy.signal
import csv
import japanize_matplotlib  # 日本語フォント対応

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--frame_period", type=float, default=5.0)
parser.add_argument("-s", "--speed", type=int, default=1)
parser.add_argument("--num_files", type=int, default=1, help="Number of files to process")

EPSILON = 1e-8

def save_statistics_csv(filename, statistics):
    """Save the F0 statistics (mean, max, min, std, median, accent) into a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Mora', 'Mean', 'Max', 'Min', 'Std', 'Median', 'Accent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for stat in statistics:
            writer.writerow(stat)

def savefig(filename, f0, frame_period, alignment, accents):
    plt.figure(figsize=(12, 6))

    mora_centers = []
    f0_means = []

    statistics = []  # To store the statistics for each phoneme

    for (start, end, label), accent in zip(alignment, accents):
        start_idx = int(start * 1000 / frame_period)
        end_idx = int(end * 1000 / frame_period)

        if start_idx < 0:
            start_idx = 0
        if end_idx > len(f0):
            end_idx = len(f0)

        if label == '、':
            f0_values = np.array([0])  # For commas, set F0 values to zero
        else:
            f0_values = f0[start_idx:end_idx]
            f0_values = f0_values[f0_values > EPSILON]  # Filter out zero F0 values

        if len(f0_values) > 0:
            f0_mean = np.mean(f0_values)
            f0_max = np.max(f0_values)
            f0_min = np.min(f0_values)
            f0_std = np.std(f0_values)
            f0_median = np.median(f0_values)
        else:
            f0_mean = f0_max = f0_min = f0_std = f0_median = 0

        center = (start + end) / 2
        mora_centers.append(center)
        f0_means.append(f0_mean)

        # Store the statistics for this mora
        statistics.append({
            'Mora': label,
            'Mean': f0_mean,
            'Max': f0_max,
            'Min': f0_min,
            'Std': f0_std,
            'Median': f0_median,
            'Accent': accent
        })

        plt.axvline(x=start, color='gray', linestyle='--', alpha=0.7)
        plt.axvline(x=end, color='gray', linestyle='--', alpha=0.7)
        plt.text(center, plt.ylim()[1] * 0.9, label, ha='center', va='bottom', fontsize=10, color='red')

    plt.plot(mora_centers, f0_means, '-o', color='red', label="平均F0", markersize=8)
    plt.xlabel("Time (s)", fontsize=14)
    plt.ylabel("F0 (Hz)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.legend(loc="upper right", fontsize=12)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return statistics

def read_accent_data(filepath):
    """Read accent data from onsoretu_split.csv file."""
    accent_data = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            accent_data.append(row)
    return accent_data

def main(args):
    # Output directories for statistics and figures
    result_dir = 'fix_heikin_result_5000'
    csv_dir = 'fix_f0_stac_result_5000'
    
    if os.path.isdir(result_dir):
        rmtree(result_dir)
    if os.path.isdir(csv_dir):
        rmtree(csv_dir)
        
    os.mkdir(result_dir)
    os.mkdir(csv_dir)

    # Load accent data from onsoretu_split.csv
    accent_filepath = 'jsut_accent_onsoretu/onsoretu_re_re_fi_split.csv'
    accent_data = read_accent_data(accent_filepath)

    # Limit the number of files to process
    alignment_dir = 'align_result_5000'
    alignment_files = sorted([f for f in os.listdir(alignment_dir) if f.endswith('.csv')])[:args.num_files]

    for i, alignment_file in enumerate(alignment_files):
        base_filename = os.path.splitext(alignment_file)[0]
        audio_file = f'basic5000/BASIC5000_{base_filename[-4:]}.wav'
        alignment_path = os.path.join(alignment_dir, alignment_file)

        # Load the audio file
        x, fs = sf.read(audio_file)

        # Resample the waveform
        new_frame_period = args.frame_period
        new_fs = int(fs * (5.0 / new_frame_period))
        new_x = scipy.signal.resample(x, int(len(x) * (new_fs / fs)))

        # Extract F0, spectral envelope, and aperiodicity using WORLD
        f0, sp, ap = pw.wav2world(x, fs)
        y = pw.synthesize(f0, sp, ap, fs, 5.0)

        # Read alignment data
        alignment = []
        with open(alignment_path, 'r') as f:
            next(f)  # Skip header
            for line in f:
                start, end, mora = line.strip().split(',')
                alignment.append((float(start), float(end), mora))

        # Get corresponding accent data for this file
        accents = accent_data[i]

        # Save F0 plot and statistics
        statistics = savefig(f'{result_dir}/fix_f0_heikin_result_{i+1}.png', f0, new_frame_period, alignment, accents)
        
        # Save the statistics to a CSV file
        save_statistics_csv(f'{csv_dir}/fix_f0_statistics_{i+1}.csv', statistics)

    print(f'{args.num_files} ファイルの処理が完了しました。出力は {result_dir} および {csv_dir} ディレクトリに保存されています。')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
