import pandas as pd
from semopy import Model, calc_stats, semplot
import argparse

# モデル記述：潜在変数名は英語、観測変数は e1〜e6
MODEL_DESC = """
# 測定モデル
InterestInGrad =~ V10 + V11 
将来に対する関心 =~ V4 + V5 + V7 +V9
CuriosityInResearch =~ V1 + V2 + V6

# 構造モデル
InterestInGrad ~ 将来に対する関心 + CuriosityInResearch
CuriosityInResearch ~ 将来に対する関心
"""

def run_sem(data_path: str, diagram_path: str = None):
    """
    SEM（共分散構造分析）を実行して、結果と適合度指標を出力する。
    
    Parameters:
        data_path (str): CSVファイルのパス（e1〜e6の列を含む）
        diagram_path (str, optional): パス図の保存先（例: "model.png"）
    """
    # データ読み込み
    df = pd.read_csv(data_path)
    
    # # 欠損値除去（必要なら）
    # df = df.dropna()

    # モデルの構築とフィッティング
    model = Model(MODEL_DESC)
    model.fit(df)

    # パス係数（推定値）の出力
    print("\n=== Parameter Estimates ===")
    print(model.inspect())

    # 適合度指標の出力
    print("\n=== Fit Statistics ===")
    stats = calc_stats(model)
    print(stats)

    # パス図の保存（オプション）
    if diagram_path:
        semplot(model, diagram_path)
        print(f"\nModel diagram saved to: {diagram_path}")

def main():
    parser = argparse.ArgumentParser(description="SEM（共分散構造分析）を実行するスクリプト")
    parser.add_argument(
        "--data_path",
        type=str, 
        default="data.csv", 
        help="入力データCSVファイルのパス（デフォルト: data.csv）"
    )
    parser.add_argument(
        "--diagram_path",
        type=str, 
        default="sem_diagram3.png", 
        help="パス図の保存先ファイル名（デフォルト: sem_diagram3.png, 保存しない場合は空文字列）"
    )
    args = parser.parse_args()

    run_sem(args.data_path, args.diagram_path)

if __name__ == "__main__":
    main()
