import PyPDF2


def simple_merge():
    # 単純に連結
    # PdfFileMergerクラスの生成
    merger = PyPDF2.PdfFileMerger()

    # append メソッドでファイルを追加
    merger.append('data/Java.pdf')
    merger.append('data/Python.pdf')

    # write メソッドで書き出し
    merger.write('data/sample_merge.pdf')
    # close メソッドで閉じる
    merger.close()

def insert():
    # ファイルの途中に別のファイルを挿入する場合はmerge()メソッドを使う。
    # 第一引数positionに挿入するページ番号を 0 始まりで指定する。
    merger = PyPDF2.PdfFileMerger()

    merger.append('data/sample_merge.pdf')
    merger.merge(1, 'data/Python.pdf')
    merger.merge(3, 'data/Java.pdf')

    merger.write('data/sample_insert.pdf')
    merger.close()


if __name__ == '__main__':
    # 単純に連結
    simple_merge()
    # 途中に挿入
    insert()
