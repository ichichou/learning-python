from datetime import datetime

import macho2


def main(like_muscle=False):
    if not like_muscle:
        print('筋トレはすごいんだよ！！（怒）')
        main(True)
    else:
        print('よく改心した。良い子だ')
        start_comment = 'Let' start KINTORE at {}'.format(datetime.now())
