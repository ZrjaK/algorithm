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
    let T = scanner.next();
    for _ in 0..T {
        let mut n: i64 = scanner.next();
        let mut a = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
        let mut ans = 0 as i64;
        for i in 1..n+1 {
            if n % i != 0 {
                continue;
            }
            let mut j = 0;
            let mut b: Vec<i64> = Vec::new();
            while j < n {
                let mut x = 0;
                for k in j..j+i{
                    x += a[k as usize];
                }
                b.push(x);
                j += i;
            }
            ans = std::cmp::max(ans, b.iter().max().unwrap() - b.iter().min().unwrap())
        }
        println!("{}", ans);
    }
}
