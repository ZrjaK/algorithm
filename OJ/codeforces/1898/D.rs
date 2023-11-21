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
        let mut n: usize = scanner.next();
        let mut a = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
        let mut b = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
        let mut ans = 0;
        let mut mx = -1e9 as i64;
        let mut mn = 1e9 as i64;
        for i in 0..n {
            ans += (a[i] - b[i]).abs();
            mx = std::cmp::max(mx, std::cmp::min(a[i], b[i]));
            mn = std::cmp::min(mn, std::cmp::max(a[i], b[i]));
        }
        println!("{}", ans + std::cmp::max(0, 2 * (mx - mn)));
        
    }
}
