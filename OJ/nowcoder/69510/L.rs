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
    let mut m: usize = scanner.next();
    let mut ans = 0;
    let mut tot = Vec::new();
    for _ in 0..n {
        m -= 1;
        let mut k: usize = scanner.next();
        let mut a = (0..k).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
        a.sort();
        ans += a.pop().unwrap();
        tot.extend_from_slice(&a);
    }
    tot.sort();
    tot.reverse();
    ans += &tot[0..m].iter().sum();
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::new();
    let T = 1;
    // let T = scanner.next();
    for _ in 0..T {
        solve(&mut scanner);
    }
}
