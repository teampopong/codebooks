POPONG Codebooks
================

Codebooks used for data at Team POPONG.

### 지역코드 (Regional codes)
- [`cb-administrative-divisions-20121231-v20130415.csv`](http://raw.github.com/teampopong/codebooks/master/cb-administrative-divisions-20121231-v20130415.csv)
    - 출처: [통계청](http://kostat.go.kr/kssc/board_notice/BoardAction.do?method=list&board_id=3&catgrp=kssc&catid1=kssc06&catid2=kssc06a)
    - 내용: 행정구역분류와 행정기관 및 법정동코드 연계표
    - 기준일: 2012-12-31
    - 최종수정일: 2013-04-15

### 기관코드 (Institutional codes)
- [`cb-higher-education-institutes-d20130501.csv`](http://raw.github.com/teampopong/codebooks/master/cb-higher-education-institutes-d20130501.csv)
    - 출처: [안정행정부 행정표준코드관리시스템](http://www.code.go.kr/std/jsp/stdcode/orgCodeL.jsp)
    - 내용: 국내 고등교육기관 코드
    - 저장일: 2013-05-01
    - 가공된 버젼:
        - 파일명: [`cb-higher-education-institutes-d20130501-unique.csv`](http://raw.github.com/teampopong/codebooks/master/cb-higher-education-institutes-d20130501-unique.csv)
        - 처리코드: `code/highereducation.py`
        - 내용: 원본에서 상위기관들의 코드만 선택

