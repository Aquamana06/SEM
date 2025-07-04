import pandas as pd
from semopy import Model, calc_stats, semplot


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
    # データファイルのパス（例：e1〜e6が入ったCSV）
    data_file = "data.csv"  # 例：columns=["e1", "e2", ..., "e6"]

    # パス図を保存する場合（不要なら None）
    output_diagram = "sem_diagram3.png"

    # 分析実行
    run_sem(data_file, output_diagram)


if __name__ == "__main__":
    main()