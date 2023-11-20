#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unused_must_use)]
#![allow(unused_mut)]

use std::{io::Read, vec::IntoIter};
struct Scanner {
    iter: IntoIter<String>,
}

impl Scanner {
    fn new() -> Scanner {
        let mut source = Vec::new();
        std::io::stdin().read_to_end(&mut source).unwrap();
        return Scanner {
            iter: source
                .split(|x| (*x as char).is_ascii_whitespace())
                .map(|x| String::from_utf8(x.to_vec()).unwrap())
                .filter(|x| !x.is_empty())
                .collect::<Vec<String>>()
                .into_iter(),
        };
    }
    fn next_string(&mut self) -> String {
        return self.iter.next().unwrap();
    }
    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        <T as std::str::FromStr>::Err: std::fmt::Debug,
    {
        return self.next_string().parse::<T>().unwrap();
    }
}
fn main() {
    let mut scanner = Scanner::new();
    let T = 1;
    // let T = scanner.next();
    for _ in 0..T {
        let mut n: usize = scanner.next();
        let mut m: i64 = scanner.next();
        let mut cnt = vec![0 ; 1e6  as usize + 1];
        for _ in 0..n {
            let h: usize = scanner.next();
            let c: usize = scanner.next();
            cnt[h] += 1;
            cnt[c] -= 1;
        }
        let mut ans = 0;
        for i in (1..1e6 as usize + 1).rev() {
            let t = std::cmp::min(m, cnt[i]);
            m -= t;
            ans += t * (i as i64 * 2 - 1);
            cnt[i - 1] += cnt[i];
        }
        println!("{}", ans);
    }
}
