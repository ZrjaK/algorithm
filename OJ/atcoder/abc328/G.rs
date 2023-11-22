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

fn solve(scanner: &mut Scanner) {
    let mut n: usize = scanner.next();
    let mut C: i64 = scanner.next();
    let mut A = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
    let mut B = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
    let mut dp = vec![std::i64::MAX; 1 << n];
    dp[0] = -C;
    for mask in 0..1 << n {
        for i in (0..n).filter(|x| mask >> x & 1 == 0) {
            let mut cost = 0;
            let mut nmask = mask;
            let c = (mask as u32).count_ones() as usize;
            for j in i..n {
                if mask >> j & 1 == 1 {
                    break;
                }
                nmask |= 1 << j;
                cost += (B[c + j - i] - A[j]).abs();
                dp[nmask] = std::cmp::min(dp[nmask], dp[mask] + cost + C);
            }
        }
    }
    println!("{}", dp.last().unwrap());
}

fn main() {
    let mut scanner = Scanner::new();
    let T = 1;
    // let T = scanner.next();
    for _ in 0..T {
        solve(&mut scanner);
    }
}
