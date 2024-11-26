+++
title = '2024 ICPC Seoul Regional 후기'
date = 2024-11-27T00:54:24+09:00
draft = false
+++

## Intro 

원래는 UCPC 2024에 도전했다가 뜨거운 실패의 맛을 보고, 팀도 깨져서 올해 ICPC는 포기하고 팀 대회는 군대나 다녀와서 시작할 생각이었습니다. 하지만...

<img src="/images/icpc-2024-seoul/Screenshot 2024-11-27 at 12.58.00 AM.png">

우연히 평소 알고만 지내던 AlKon 동아리 2학년 <span style="color: #a0a !important">**motsuni04**</span>에게 연락이 왔습니다. (이 때는 몰랐지만) 작년 ICPC 팀원이었던 <span style="color: gray !important">**s6xybr8in**</span>님이 군입대를 하게 되셔서 제가 들어오게 되었습니다. 든든한 버스기사 <span style="color: #FF8C00 !important">**yookwi**</span>도 합류해서 팀이 결성되었습니다!

<img src="/images/icpc-2024-seoul/Screenshot 2024-11-27 at 1.13.48 AM.png">

팀연습은 보통 업다운 랜디, USACO나 ICPC 기출셋, Codeforces Div.2 등등 다양하게 하였고, 세종대 <span style="color: #a0a !important">**pizzaroot**</span>랑 팀원 분들도 가끔 같이 연습했었습니다. 공강이 겹치는 시간에 PC방에서 같이 Codeforces 버추얼을 쳤던 기억도 나네요 ㅋㅋ

보통 팀연습을 하면 <span style="color: #FF8C00 !important">**yookwi**</span>가 문제가 구데기같다면서 투덜거리며 가장 먼저 풀고, 구현이 빠른 <span style="color: #a0a !important">**motsuni04**</span>가 따라 풀고, 저는 대부분 못 풀어서 팀원들에게 배우거나 풀어도 가장 늦게 풀었습니다.

팀연습에서 가장 어려웠던 점은 대회 환경으로 인해 C++이 강제되었다는 것인데요, 저는 주력 언어가 Rust였고, C++ 특유의 불친절한 디버깅과 Undefined Behavior지만 돌아가긴 해서 생기는 문제들의 대환장 콜라보로 정말 많이 힘들었습니다. (변명 아님)

그래도 같이 연습하는 동안 DP와 이분탐색 등 기본적인 실력이 많이 늘었고, 문제를 바라보고 해결하는 인사이트도 늘었습니다. 또, 구현 능력도 좋아진 것 같아서 보람이 있었습니다. 팀 분위기도 좋았던 것 같고 정말 소중한 시간이었습니다.

BusTaeWarJo라는 팀명은 AlKon 회장님이 정해주신 대회 접수 마감기한 3분 **후**까지도 정하지 못했다가 막 지었습니다. <span style="color: #FF8C00 !important">**yookwi**</span>가 버스기사입니다.

<hr>

## 온라인 예선

예선은 치른 지 조금 오래됐기도 했고, 제가 정말 버스만 타서 기억도 별로 없어서 간략하게 적겠습니다. 학교 근처에서 점심을 먹고, 편의점에서 대회 중에 먹을 과자를 샀습니다. 원래 학교 K-Cube라는 스터디 룸을 예약했는데, 생각보다 환경이 좋지 않았고, 심지어 근처 교내 프린트 가게가 주말이라 전부 문을 닫아서 재빨리 근처 스터디 카페를 예약해서 장소를 옮겼습니다.

[예선 문제셋 (BOJ)](https://www.acmicpc.net/category/detail/4344)

> 어떤 이유에서인지, K번이 아직 안 올라왔습니다. [이곳에서](https://icpckorea.org/static/2024_problemset.pdf) 전 문항 pdf를 볼 수 있습니다.

**E (00:06)**

저는 대회가 시작되자마자 스터디 카페 프린터로 문제지를 인쇄하러 갔습니다. 그 사이 다른 팀원들이 문제지의 한국어 문제가 있는 페이지들을 모아놓고 읽어보다가 가장 쉬워보여서 <span style="color: #a0a !important">**motsuni04**</span>가 빠르게 풀었다고 합니다.

**H (00:35) +1**

마찬가지로 한국어 문제입니다. <span style="color: #FF8C00 !important">**yookwi**</span>가 백트래킹으로 풀었습니다.

**F (00:55)**

이것도 한국어 문제입니다. 누가봐도 기하라 미뤄두려다가, <span style="color: #a0a !important">**motsuni04**</span>가 간단한 풀이를 찾아 빠르게 구현했습니다. 이때쯤 저는 D를 잡고 있었습니다.

**C (01:09)**

<span style="color: #FF8C00 !important">**yookwi**</span>가 종이에 조금 적어보더니, 아는 문제라고 세그먼트 트리와 KMP를 빠르게 구현하여 AC를 받았습니다. 이정도면 본선컷은 넘길 수 있겠다는 생각에 기뻤습니다. 하지만... (후술)

**C (02:39) +7**

저는 잡고있던 D가 그리디 문제고, 대각선끼리 만나는 교점을 가지고 비벼보면 될 것 같단 생각을 했지만, 팀원들에게 관찰한 내용을 말해주니 2-SAT 같다면서 버리자고 했습니다. 이후 <span style="color: #FF8C00 !important">**yookwi**</span>가 저에게 MST 쓰는 문제 같으니 C번을 잡아보라고 줬지만, 20분동안 별 진전이 없었습니다. 다시 <span style="color: #FF8C00 !important">**yookwi**</span>에게 C번을 넘기고 이때까지 저와 <span style="color: #a0a !important">**motsuni04**</span>는 K번의 상한이 생각보다 널널하다는 점을 관찰해 풀이를 대충 알아냈고, 코드까지 공책에 적었지만 <span style="color: #FF8C00 !important">**yookwi**</span>가 맞왜틀을 하며 테스트 케이스를 만들어주는 데 올인했습니다. 팀노트를 대회 하루 전 <span style="color: #FF8C00 !important">**yookwi**</span>가 정말 대충 만들어왔는데, 정말 운이 좋게도 단절점/단절선 알고리즘이 있어서 유용하게 사용했습니다. 7번의 시도 끝에 결국 C를 풀고 스코어보드를 보니 본선 진출이 확정되었습니다. 너무 재밌었습니다.

이후 마침 근처에서 예선을 치른 AlKon 회장 **dldyou**님과 <span style="color: #a0a !important">**pizzaroot**</span> 팀이랑 저녁식사를 했습니다. 양식집이었는데, 피자와 파스타를 정말 맛있게 먹었습니다. 그 다음날 있을 정보보안 동아리 대회에서 출제를 하시게 된 **dldyou**님과 학부생 연구원 일로 바쁘신 **javago**님은 먼저 가시고, 나머지는 보드게임 카페에 가서 능지대결을 펼쳤습니다.

이후 예선 19등으로 마무리하는 줄 알았지만, C번 정해에 이상이 있었다는 것이 발견되고, 재채점 결과 25등으로 마무리하게 되었습니다... 뭐 본선 진출은 했으니 된 거 아닐까요 ㅎㅎ;

## 본선

시험 기간이 끝나고 본 대회를 위해 다시 열심히 연습했습니다. 저는 도널드 커누스의 이산 수학 책인 <구체 수학 (Concrete Mathematics)>과 건국대학교 수학과 정수론 전공서적, 중학교 수학 올림피아드 기출문제들을 통해 살짝 따로 수학을 공부했습니다.

팀노트도 새로 만들었습니다. 배워야 쓸 수 있는 너무 어려운 알고리즘들은 쳐내고, 실용적으로 구성했습니다.

예비소집날 저는 합정에서 M7731 버스를 타고 갔는데, 우연히 <span style="color: #FF8C00 !important">**yookwi**</span>를 만나서 같이 갔습니다. 뭔가 학생들처럼 보이는 사람들이 킨텍스 제1전시장쪽으로 가서 속을 뻔 했지만 (다른 행사가 있었나봅니다), 상당히 여유롭게 도착했습니다. ICPC 관련 현수막은 없고 블루 아카이브 3주년 축제 현수막이 대문짝만하게 걸려있어서 잘못 온 줄 알았습니다 ㅎㅎ;

<img src="/images/icpc-2024-seoul/IMG_6823.JPG">

~~저기갈걸~~

등록을 마치고, 대기실에서 포커, 테트리스, 리듬게임, 롤 등 다양하게 즐기다가 연습 세션 문제를 빠르게 풀고 나왔습니다. 모니터도 아래로 꺾여 있었고, 키보드 키감이 정말... 최악이라 스탭분께 다이소에서 키보드 하나 사와도 되나 여쭤봤지만 안 된다고 하셨습니다. 인형같은 개인용 토템을 들고 오신 분들도 계셨는데, 반입이 가능한 줄 알았으면 저도 하나 가져올 걸 하는 생각이 듭니다. 참고로 저희 팀은 Visual Studio Code를 사용하기로 했고, 제가 Vim 익스텐션을 켜놨다가 한 대 맞을 뻔 했습니다. CPH (<span style="color: #FF8C00 !important">**yookwi**</span>는 CHP라고 부릅니다) 익스텐션이 없는 게 조금 아쉬웠지만, 그럭저럭 좋았습니다.

<img src="/images/icpc-2024-seoul/IMG_6840.JPG">

테트리스도 질려서 이제 할 일도 없는데 <span style="color: #a0a !important">**pizzaroot**</span> 팀은 아직 뭔가 열심히 하고 있어서, 제가 장미 접는 법을 <span style="color: #FF8C00 !important">**yookwi**</span>에게 전수해주었고, 결국 받은 문제지로 몽땅 장미를 접어놓고 나왔습니다. 예쁘죠? ㅎ

연습 세션이 끝나고 대회장을 나와서 <span style="color: #a0a !important">**pizzaroot**</span> 팀과 또 저녁을 먹었습니다. 대화역 근처 노랑통닭을 갔는데 치킨으로 정말 배부르게 먹었습니다.

이후 킨텍스와 조금 떨어져있는 숙소로 가서 짐을 풀고, 근처 홈플러스에서 야식, 다음날 아침에 먹을 크리스피 도넛, 대회 중에 먹을 간식을 샀고 신나게 팀연습 (랜디 잠깐 하다가 앳코더 풀이 시청)도 하고 게임을 하다가 잤습니다. 제가 저녁을 먹었던 노랑통닭집에 휴대폰을 놓고 나오는 앙증맞고 사소한 일이 있었지만 대형 사고는 아니었습니다.

<img src="/images/icpc-2024-seoul/IMG_6848.JPG">

다음날 아침 <span style="color: #a0a !important">**motsuni04**</span>가 침대에서 이불탐색을 하다가 TLE가 날 뻔한 앙증맞고 사소한 일이 있었지만 원만하게 잘 해결되었고, 택시를 타고 대회장까지 갔습니다. 9300원밖에 안 나왔는데 버스보다 2배 빨랐으니 본전 아닌가 싶습니다.

다행히 늦지 않게 등록을 마쳤고, <span style="color: #FF8C00 !important">**yookwi**</span>가 작년에 늦게 입장했다가 간식을 받지 못하는 대참사가 발생했다고 앞에 앉자 해서 제일 앞에 앉았습니다. (사실 올해는 간식이 없었고 물만 줬지만요)

대회장에 가장 들어갔지만, 참가자들이 들어오는 속도가 생각보다 느려서 대회가 연기되었고, 저희 팀은 풍선의 개수, 색깔, 배치와 문제 난이도와의 상관관계를 예측하는 쓰잘데기 없는 짓으로 시간을 떼우다가 (사실 의미가 있었습니다!) 대회가 시작되었습니다.

[본선 문제셋 (BOJ)](https://www.acmicpc.net/category/detail/4348)

**A (00:18) +1**

제가 잡은 문제가 되게 쉬워보여서, 쉬운 문제를 빠르게 구현할 수 있는 <span style="color: #a0a !important">**motsuni04**</span>에게 넘겨주었습니다. 구현이 지저분하다고 궁시렁거리면서 1번 틀리고 열심히 반례를 찾다가 결국 AC. 나중에 훨씬 간단한 풀이를 찾았다면서 좋아했습니다. 대회 전 A번 풍선이 ICPC를 상징하는 빨간색, 노란색, 파란색 풍선 중 하나라 A번이 쉬워보인다고 말했었지만, 진짜 가장 쉬운 문제일 줄은 상상도 못했습니다...

**B (00:34) +1**

이 문제는 제가 잡다가 그리디인 줄 알고 삽질했는데, <span style="color: #FF8C00 !important">**yookwi**</span>가 가져가서 빠르게 풀었습니다. 살다살다 이런 구현을 다 해본다고 하길래 나중에 알아보니 맵을 가지고 BFS를 돌리는 풀이를 짜냈다고 합니다 ㅋㅋ.

**L (01:03)**

이 문제도 처음에는 제가 잡았다가, 상위권 팀이 너무 빨리 풀어버려서, 새로운 삼각형을 만들 수 있는 격자점들이 $\gcd (\vert x_i - x_j \vert, \vert y_i - y_j \vert)$의 배수만 가능하다는 간단한 관찰과 함께 <span style="color: #a0a !important">**motsuni04**</span>에게 넘겨주었습니다. 구현을 잘 해서 다행히 한 번에 맞았습니다.

**J (01:50) +2**

<span style="color: #FF8C00 !important">**yookwi**</span>와 <span style="color: #a0a !important">**motsuni04**</span> 둘이 풀었습니다. 맞왜틀을 하면서 많이 고생했던 것으로 기억합니다. 저는 E를 풀었고, <span style="color: #FF8C00 !important">**yookwi**</span>에게 풀이를 설명했지만, 다익스트라를 쓸 생각을 해서 시간 안에 안 돌거라고 빠꾸를 먹고, 수학으로 구할 수 있다고 했지만, Convex Hull까지 구현에 동원하기 무서워 미뤄두기로 했습니다.

**F (03:01) +2**

<span style="color: #FF8C00 !important">**yookwi**</span>의 오더로 저와 <span style="color: #a0a !important">**motsuni04**</span>가 손으로 직접 $n$이 작을 때를 직접 해보면서 규칙성을 찾아봤습니다. 처음에는 귀납적으로 증명할 수 있나 했지만, $0.7(n+1)^2 - 0.7n^2 = 1.4n + 0.7$, $n$번째가 정렬된 상태로 $n+1$ 페어를 추가해도 제한 안에 옮길 수 없다는 것을 확인했습니다. <span style="color: #a0a !important">**motsuni04**</span>가 꽤 적은 횟수로 정렬하는 데 성공했지만, 일관적으로 풀 수 없어서 한참을 더 잡고 있었고, 기적적으로 지그재그로 원소 $1$하나를 $1$번 인덱스에 갖다넣으면 이쁜 모양이 나오는 것을 관찰해서 <span style="color: #FF8C00 !important">**yookwi**</span>에게 넘겨주었습니다. <span style="color: #FF8C00 !important">**yookwi**</span>가 생각보다 빠르게 구현했지만, WA를 받았습니다. 셋이서 한참 디버깅을 한 후에, <span style="color: #FF8C00 !important">**yookwi**</span>가 결국 문제점을 찾았습니다. swap 연산을 하기 전에 출력했어야 했지만, swap 연산 이후에 출력을 해버려서 틀렸던 것이었습니다. 코드 두 줄의 순서를 바꿔서 AC를 받았습니다. 생각보다 종이에 쓸 게 많아서 풀고나서 손이 조금 아팠습니다.

이후로는 계속 C를 열심히 잡다가 TLE가 나올 각오로 제출해보았지만 WA를 받았고, E에 미련이 남은 제가 별찍기 코드를 제출해서 WA를 받고 5솔브 38위라는 조금 아쉬운 성적으로 대회가 종료되었습니다.

<img src="/images/icpc-2024-seoul/IMG_6861.JPG">

온사이트 대회 최고의 관람 포인트는 스코어보드 오픈이 아닐까 싶습니다. 저희 팀이 나올 때만 빼고 짜릿했습니다.

<img src="/images/icpc-2024-seoul/Screenshot 2024-11-27 at 3.58.58 AM.png">

풀이 세션과 Tech Talk 등 남은 일정들이 마무리되고, 같이 저녁식사를 하고 각자 집 가는 길이 달라서 헤어졌습니다. 마침 블루 아카이브 축제가 끝나는 시간과 겹쳐서... 매우 지옥같은 킨텍스 교통을 맛볼 수 있었습니다.

이 글을 작성하고 있는 지금도 저는 대회 준비했을 때만큼 열심히 알고리즘 공부를 하고 있습니다. 문제를 봐도 접근조차 하지 못해 팀원에게 떠넘기기만 하고, 잘 하지 못해 팀원들에게 너무 미안했습니다. 정말 팀명대로 제가 버스를 타버린 것입니다. 분명 AlKon 동아리에 저보다 잘 하는 분들도 많은데, 한편으론 불러줘서 고마웠고, 연습 내내 배우면서 성장할 수 있어서 좋았습니다. 정말 잊지 못할 즐거운 경험이었던 건 분명합니다.

저는 내년에 2학년 1학기를 마치고 입대를 할 예정입니다. 군대에서도 꾸준히 알고리즘을 공부해서 2, 3, 4학년때 ICPC에서 지금보다 더 좋은 성적을 받아 꼭 입상하고 싶습니다. 아무튼 긴 글 읽어주셔서 감사합니다.