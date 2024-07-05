+++
title = '등비수열의 합을 빠르게 구하기'
date = 2024-07-04T17:56:40+09:00
draft = false
categories = ["알고리즘"]
tags = ["ps", "정수론", "dac", "수학"]
+++

## Intro

등비수열 $a_{n} = ar^{n-1}$의 합은
$$
S_n = \begin{cases}
   an &\text{if } r=1\\ \newline 
   \frac{a(r^n - 1)}{r-1} &\text{otherwise}
\end{cases}
$$
로 나타낼 수 있습니다.\
$r=1$일 때 $S_n$이 다른 이유는, $\frac{a(r^n - 1)}{r-1}$의 분모가 $0$이 되기 때문입니다.\
이때는, $1$항부터 $n$항까지가 모두 $a$로 같으니, 간단하게 $an$으로 나타낼 수 있습니다.

<img src="/images/kikuri/52.png" width="100" height="100">

$n$이 커지면 커질 수록 $S_n$은 (말 그대로) 기하급수적으로 커지기 때문에, 일반적으로 PS에서는 $S_n$을 $m$으로 나눈 나머지를 구하도록 합니다.

따라서, 이 글에서는 등비수열의 합 $S_n\ \textrm{mod}\ m$을 빠르게 구할 방법을 소개하겠습니다.

<img src="/images/kikuri/5.png" width="100" height="100">

-----
## 모듈로 곱셈 역원 ($m$은 소수)

정수 $a$와 소수 $p$에 대하여, $a$와 $p$가 서로소일 때, 법 $p$에 대하여 $a$의 <b>곱셈 역원</b> $a^{-1}$이 유일하게 존재합니다.\
즉, $aa^{\prime} \equiv 1\ (\textrm{mod}\ p)$을 만족하는 역원을 $a^{-1}$라고 합니다.

그렇다면, <b>페르마의 소정리</b>
$$
a^{p-1} \equiv 1\enspace\ (\textrm{mod}\ p)
$$
를 이용하여 이 역원을 구해봅시다.

양변에 $a^{-1}$을 곱하면, $a^{p-2} \equiv a^{-1}\ (\textrm{mod}\ p)$가 됩니다.\
$a$의 역원 $a^{-1}$을 양변에 곱하는 것과 양변에 $a$를 나누는 것이 같음을 보일 수 있지만, 증명은 생략하겠습니다. (증명이 궁금하다면, 이미 구글에도 좋은 자료가 많고, 정수론 책을 찾아봐도 좋습니다.)

조금 어려울 수도 있지만, 이런 게 있다는 정도만 알고 넘어갑시다.

<img src="/images/kikuri/18.png" width="100" height="100">

따라서, 등비수열의 합 $S_n = \frac{a(r^n - 1)}{r-1}$은 법 $m$에 대해 $S_n \equiv a(r^n -1)(r - 1)^{m - 2}\ (\textrm{mod}\ m)$으로 나타낼 수 있습니다.

페르마의 소정리를 이용하여 역원을 구하면 나눗셈을 곱셈으로 바꿀 수 있어서 편리하지만, 지수가 너무 커져서 거듭제곱 계산에 많은 시간이 들어갈 것으로 보입니다.

하지만, 여기서 $a^b\ \textrm{mod}\ c$를 빠르게 계산할 수 있는 테크닉이 있습니다.

<img src="/images/kikuri/3.png" width="100" height="100">

바로 <b>'분할 정복을 이용한 거듭제곱'</b>이라고 하는 테크닉인데요,
$$
a^n = \begin{cases}
   a^{\frac{n}{2}} \times a^{\frac{n}{2}} & \textrm{if } n\textrm{ is odd}\\ \newline 
   a^{\lfloor \frac{n}{2} \rfloor} \times a^{\lfloor \frac{n}{2} \rfloor} \times a & \textrm{if } n\textrm{ is even}
\end{cases}
$$
위와 같이 $a^n$의 지수를 반으로 쪼개고, 구한 값을 바탕으로 다시 합치면, 거듭제곱 계산을 $\mathcal{O}(n)$에서 $\mathcal{O}(\lg n)$으로 줄일 수 있습니다! (여기서 $\lg$는 밑이 $2$인 로그, $\log _{2}$를 의미합니다.)

<img src="/images/kikuri/11.png" width="100" height="100">

따라서, $m$이 소수일 때에는 분할 정복을 이용한 거듭제곱을 이용하여, $S_n\ \textrm{mod}\ m$을 $\mathcal{O}(\lg n)$에 구할 수 있습니다.

-----
## 분할 정복
$m$이 만약 소수가 아니라면 어떨까요? 아쉽게도 여기서는 모듈로 곱셈 역원을 구하는 방법을 사용할 수 없습니다.

<img src="/images/kikuri/24.png" width="100" height="100">

$a$와 $m$이 서로소가 아니라면, $aa^{\prime} \equiv 1\ (\textrm{mod}\ m)$을 만족하는 역원이 존재할 수 없기 때문입니다.\
증명은 마찬가지로 생략하겠습니다.

따라서, 합 공식을 사용하는 것은 불가능해보이고, 모든 항을 일일이 더하기에는 너무 느릴 것 같습니다.

그렇다면 $S_n$의 정의로 돌아가볼까요?
$$
\begin{align*}
S_n & = a_1 + a_2 + \cdots + a_n\\ \newline
& = a + ar + ar^2 + \cdots + ar^{n-1}
\end{align*}
$$
사실 $S_n$은 제 $1$항부터 $n$항까지 더한다는 기호일 뿐인데, 많은 사람들이 $S_n$의 정의를 그냥 지나치고, 합 공식만 활용하려고 하는 모습을 저는 많이 봐왔습니다. 본질로 돌아가 봅시다.\
$S_n$을 풀어 헤쳐봤으니, 등비수열의 성질을 이용해 식을 간략하게 만들어봅시다.

<img src="/images/kikuri/25.png" width="100" height="100">

먼저, $n$이 짝수일 때에는,
$$
\begin{align*}
S_n & =a+ar+ar^2+\cdots+ar^{n-1}\\ \newline
& =(a+ar+\cdots+ar^{\frac{n}{2}-1})+(ar^{\frac{n}{2}}+ar^{\frac{n}{2}+1}+\cdots+ar^{n-1})\\ \newline
& =(a+ar+\cdots+ar^{\frac{n}{2}-1})+ r^{\frac{n}{2}}(a+ar+\cdots+ar^{\frac{n}{2}-1})\\ \newline
& =(a+ar+\cdots+ar^{\frac{n}{2}-1})(1+r^{\frac{n}{2}})\\ \newline
& =S_{\frac{n}{2}}\cdot (1+r^{\frac{n}{2}})
\end{align*}
$$
이렇게 식의 규모를 딱 반으로 줄일 수 있습니다. 식이 반씩 줄어드니, 시간복잡도는 $\mathcal{O}(n)$에서 $\mathcal{O}(\lg n)$로 줄어들겠네요.\
$(1+r^{\frac{n}{2}})$는 따로 '분할 정복을 이용한 거듭제곱'을 통해 $\mathcal{O}(\lg n)$에 구할 수 있습니다.

$n$이 홀수일 때에는 $S_n$을 정확히 반으로 묶어낼 수 없으므로,
$$
\begin{align*}
S_n & =(a+ar+\cdots+ar^{n-2})+ar^{n-1}\\ \newline
& =S_{n-1}+ ar^{n-1}
\end{align*}
$$
으로 정리하고, $n-1$은 짝수이므로, $S_{n-1}$은 위의 짝수일 때의 경우를 이용하여 똑같이 처리하고, $ar^{n-1}$ 역시 '분할 정복을 이용한 거듭제곱'을 통해 $\mathcal{O}(\lg n)$에 구할 수 있습니다.

<img src="/images/kikuri/22.png" width="100" height="100">

즉, $S_n$을 분할 정복을 이용하여 구하려면,
$$
S_n = \begin{cases}
   S_{n-1}+ ar^{n-1} & \textrm{if } n\textrm{ is odd}\\ \newline 
   S_{\frac{n}{2}}\cdot (1+r^{\frac{n}{2}}) & \textrm{if } n\textrm{ is even}
\end{cases}
$$
으로 표현할 수 있고, 시간복잡도는 $\mathcal{O}(\lg n)$이 됩니다!

-----
## 요약

- $m$이 소수라면?

$S_n \equiv a(r^n -1)(r - 1)^{m - 2}\ (\textrm{mod}\ m)$ 이용.

- $m$이 소수인지에 관계없이,

$$
S_n = \begin{cases}
   S_{n-1}+ ar^{n-1} & \textrm{if } n\textrm{ is odd}\\ \newline 
   S_{\frac{n}{2}}\cdot (1+r^{\frac{n}{2}}) & \textrm{if } n\textrm{ is even}
\end{cases}
$$
을 이용하여 $S_n\ \textrm{mod}\ m$을 $\mathcal{O}(\lg n)$에 구할 수 있습니다!

<img src="/images/kikuri/17.png" width="100" height="100">

-----
## 연습문제
[BOJ 30413 - 양 한 마리... 양 A마리... 양 A제곱마리...](https://www.acmicpc.net/problem/30413)\
등비수열의 합을 $10^9+7$로 나눈 나머지를 구하는 문제입니다. 문제 조건에서, 춘배는 똑똑해서 $10^9+7$이 소수임을 알고 있다고 하니, 페르마의 소정리를 활용하여 쉽게 구할 수 있겠습니다. $r=1$인 상황을 주의합시다.

[BOJ 15712 - 등비수열](https://www.acmicpc.net/problem/15712)\
이번에는 문제 입력으로 들어오는 $\textrm{mod}$가 소수라는 보장이 없습니다!
분할 정복으로 빠르게 구해봅시다.

[BOJ 1160 - Random Number Generator](https://www.acmicpc.net/problem/1160)\
점화식 $X_{n+1} = (aX_n + c) \mod m$을 직접 전개하다 보면 중간에 등비수열이 하나 보입니다. 역시 $m$이 소수라는 보장이 없기 때문에, 분할 정복으로 합을 구해봅시다.
