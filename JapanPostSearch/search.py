import argparse

# --postal_codeのみ指定：郵便番号から検索することが可能
# --addressesのみ指定：住所から郵便番号を検索することが可能
# 両方指定：両方のデータを用いて検索することが可能
def search(postal_code, addresses):
    output_data = []
    # CSVファイルを開く
    with open('data\KEN_ALL.CSV', 'rt', encoding='shift_jis') as fp:
        for line in fp:
            line = line.replace(' ', '') # 空白を削除
            line = line.replace('"', '') # ダブルクォーテーションを削除
            cells = line.split(',')
            # 郵便番号を取得
            csv_postal_code = cells[2]
            # 都道府県を取得
            prefectures = cells[6]
            # 市区を取得
            streets = cells[7]
            # 市区以下を取得
            towns = cells[8]
            address = prefectures + streets + towns
            if postal_code:
                if postal_code == csv_postal_code:
                    output_data.append((csv_postal_code, address))
            if addresses:
                if addresses in address:
                    output_data.append((csv_postal_code, address))

    # 重複は削除してから表示する
    for output in list(dict.fromkeys(output_data)):
        print(output[0], output[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--postal_code", help="郵便番号は xxxxxxx 形式で指定すること")
    parser.add_argument('--addresses', help="住所を入力して郵便番号を検索する")
    args = parser.parse_args()
    search(args.postal_code, args.addresses)
