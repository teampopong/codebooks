#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pandas as pd

'''
- 데이터 다운로드: [기관코드조회](https://www.code.go.kr/std/jsp/stdcode/orgCodeL.jsp)
    > 기관유형선택 '고등교육기관'
    > '기관코드 조회자료' 버튼을 클릭해 파일로 저장 (ex: `cb-higher-education-institutes-d20130501.csv`)

- 데이터 처리:

        pip install pandas
        python highereducation.py
'''

inp = 'cb-higher-education-institutes-d20130501.csv'    # Input filename
outp = 'cb-higher-education-institutes-d20130501-unique.csv'
cb = pd.read_csv(inp, encoding='utf-8')

with open(outp, 'w') as f:
    f.write('code,ko\n')
    for a, b, c in zip(cb[u'기관코드'], cb[u'전체기관명'], cb[u'최하위기관명']):
        if b==c and b!=u'대학':
            s = '%s,%s\n' % (a, b)
            f.write(s.encode('utf-8'))
