### 1. 팀원 정보 및 업무 분담 내역

권종률(팀장) - FE, BE

- dj rest auth를 이용한 계정관리

- 모델 구현

- 리뷰CRUD, 댓글 대댓글 CURD, 좋아요 구현

- 프로필 구현

- 팔로우, 팔로잉 구현

정윤지(팀원) - FE, BE

- TMDB api를 이용한 영화 더미 DB 생성

- ERD 구조 설계

- 디자인 설계

- 검색창 구현

- 영화 디테일 페이지 구현

- 페인페이지 구현

### 2.  목표 서비스 구현 및 실제 구현 정도

1. 회원가입, 로그인, 로그아웃,  회원정보 변경, 비밀번호 변경

2. 홈 화면 TMDB api를 이용한 상영중인 영화 목록 표출

3. 홈 화면 자체 DB를 이용한 연도별 인기작, 장르별 최신작(연도, 장르 각각 선택 가능)

4. 영화 클릭시 디테일 페이지 - 좋아요, 줄거리, 포스터, 예고편, 출연진&감독, 댓글, 대댓글, 댓글 대댓글의 유저 사진 클릭시 프로필 이동

5. 라우터 가드를 이용한 비로그인시 이용 불가능한 사이트 차단(리뷰 CRUD (목록은 표출, 상세 페이지만 차단), 개인 프로필)

6. 리뷰 목록, 작성(영화 선택시 사진 표출), 수정, 삭제, 유저 프로필 사진 표출

7. 리뷰 디테일 페이지 좋아요, 프로필 사진 클릭시 프로필으로 연결, 영화 사진 클릭시 영화 디테일로 연결

8. 검색창 DB의 영화들을 모두 검색 후 목록에 없을 시 api서치를 이용한 검색

9. 검색 목록 영화 클릭시 영화 디테일 페이지로 이동 (디테일 페이지 또한 DB에서 검색 후 목록에 없으면 api디테일을 이용)

10. 프로필 좋아하는 장르 1개이상 3개이하 선택 가능, email, 소개글 작성, 프로필 사진 업데이트

# 구현 상세사진

![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/b4a851f0-2ac5-4fe6-8e54-8ca0ccb7cd9d)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/acf122fd-f757-4e1f-b2af-265a3914aa49)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/29e0ec94-9311-48ed-bf5c-663ae6cfa4da)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/b5fce85e-af45-4246-88cd-4f63d919f95c)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/c65a308a-9eb4-4c96-b73e-e93327bcffbd)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/c3995145-da4d-4934-883a-2eaf273faddc)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/47464756-786f-4aa2-96ef-6d1247d5fe57)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/65e5de87-13f4-4b83-acc3-dadb73161d3d)
![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/a15179bf-114e-45ea-b426-90cba515e9b7)


### 3. 데이터베이스 모델링(ERD)



![image](https://github.com/KwonJongryul/moviePjt/assets/122791001/ed934a3c-a2ce-45f3-a23a-878d357c7e39)






### 4. 영화 추천 알고리즘에 대한 기술적 설명

최신 영화 - api에 현재 상영중인 영화 정보 10개 추출

연도별 영화 - 각 연도별로 백에서 처리 후 랜덤으로 10개 추출

연도별 장르 - 각 장르별로 백에서 처리 후 최신 100개 중 랜덤으로 10개 추출

### 5. 서비스 대표 기능에 대한 설명

대표 기능이라기 보다도 기본에 충실하고 연결성 있는 페이지를 만들고 싶었던것 같습니다.

더 재미있는 기능에 대한 욕심이 없었던건 아니지만 시간과 노련함의 부족으로 이정도에서 마무리 했습니다.

### 6. 느낀점, 후기

권종률 - 복잡한 알고리즘을 통해 추천이나 다른 기능보다 보편적으로 웹사이트에 있는 기능 위주로 개발하였고, 연결성 있는 페이지를 만드려고 노력했습니다. 시간이 좀 더 있었으면 하는 아쉬움이 있지만 다음엔 좀 더 어려운 프로젝트도 도전해 보고 싶습니다.

정윤지 - 개인 사정으로 프로젝트에 온전히 집중하지 못해서 미안함과 고마움이 큽니다. 시간이 부족했지만 페이지를 하나씩 채워갈 때 마다 뿌듯하고 재밌었습니다. 직접 해보면서 많이 배웠고 어떤 부분이 부족한지 알 수 있었습니다.
