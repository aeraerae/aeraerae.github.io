+++
title = 'Test Post'
date = 2024-06-28T17:30:24+09:00
draft = false
categories = ["일상"]
+++

## 테스트 입니다.

블로그를 옮겼습니다. __기존 [블로그](https://velog.io/@aerae)는 더 이상 사용하지 않습니다.__

지금 사용중인 theme은 KaTeX 지원을 한다고 들었습니다.\
해보니까 안 돼서 직접 넣었습니다...

$$
\sin x = \sum _{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}
$$


등비수열 $ a_{n} = ar^{n-1} $의 합은 어쩌구\
잘 되네요.

Code block과 Syntax highlighting 테스트
```rust {linenos = true}
fn miller_robin(n: u64, a: u64) -> bool {
    if a % n == 0 { return true; }
    let mut k = n - 1;
    loop {
        let temp = fexp(a as u128, k as u128, n as u128) as u64;
        if temp == n - 1 { return true; }
        if k & 1 == 1 { return temp == 1 || temp == n-1; }
        k >>= 1;
    }
}
```
만족스럽습니다.

이제 글 작성에 필요한 것들은 잘 세팅이 되었네요. \
앞으로 유익하고 도움이 되는 글들로 돌아오겠습니다. 감사합니다.
