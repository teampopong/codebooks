POPONG Codebooks
================

Codebooks used for data at Team POPONG.
These codes are used in Team POPONG's service [Pokr](http://pokr.kr).

## Descriptions
### 국가공인코드

#### 기관코드 (Institution codes)
- [`cb-higher-education-institutes-d20130501.csv`](http://raw.github.com/teampopong/codebooks/master/cb-higher-education-institutes-d20130501.csv)
    - 출처: [안정행정부 행정표준코드관리시스템](http://www.code.go.kr/std/jsp/stdcode/orgCodeL.jsp)
    - 내용: 국내 고등교육기관 코드
    - 저장일: 2013-05-01
    - 가공된 버젼:
        - 파일명: [`cb-higher-education-institutes-d20130501-unique.csv`](http://raw.github.com/teampopong/codebooks/master/cb-higher-education-institutes-d20130501-unique.csv)
        - 처리코드: `code/highereducation.py`
        - 내용: 원본에서 상위기관들의 코드만 선택

#### 지역코드 (Region codes)
- [`cb-administrative-divisions-20100401.csv`](http://raw.github.com/teampopong/codebooks/master/cb-administrative-divisions-20100401.csv)
    - 출처: [통계청](http://kostat.go.kr/kssc/board_notice/BoardAction.do?method=view&board_id=3&seq=8&num=8&parent_num=0&page=2&sdate=&edate=&search_mode=&keyword=&position=&catgrp=kssc&catid1=kssc06&catid2=&catid3=&catid4=#startHeader)
    - 내용: 행정구역분류 코드 및 영문/한문 명칭
    - 기준일: 2012-04-01
    - 가공된 버젼:
        - 파일명: [`cb-administrative-divisions-20100401-edited.csv`](http://raw.github.com/teampopong/codebooks/master/cb-administrative-divisions-20100401-edited.csv)
        - 처리코드: `code/admindivisions.py`
        - 내용: 원본에서 불필요한 공백 삭제

- [`cb-administrative-divisions-20121231-v20130415.csv`](http://raw.github.com/teampopong/codebooks/master/cb-administrative-divisions-20121231-v20130415.csv)
    - 출처: [통계청](http://kostat.go.kr/kssc/board_notice/BoardAction.do?method=list&board_id=3&catgrp=kssc&catid1=kssc06&catid2=kssc06a)
    - 내용: 행정구역분류와 행정기관 및 법정동코드 연계표
    - 기준일: 2012-12-31
    - 최종수정일: 2013-04-15


### 자체생성코드
[Team POPONG](http://popong.com)에 의해 자체 생성된 코드들.
- IDs are unique random numbers, if not otherwise noted.

#### 인물코드 (Person codes)
- [`cb-people.csv`](https://github.com/teampopong/codebooks/blob/master/cb-people.csv)
- Birth year of person + random number를 기준으로 ID 부여

#### 의안상태코드 (Bill status codes)
- [`cb-people.csv`](https://github.com/teampopong/codebooks/blob/master/cb-bill-statuses.csv)

#### 정당코드 (Party codes)
- [`cb-parties.csv`](https://github.com/teampopong/codebooks/blob/master/cb-parties.csv)

#### 선거코드 (Election codes)
- [`cb-elections.csv`](https://github.com/teampopong/codebooks/blob/master/cb-elections.csv)

## License
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
