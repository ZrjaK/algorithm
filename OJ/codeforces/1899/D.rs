#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unused_must_use)]
#![allow(unused_mut)]

use std::{io::Read, vec::IntoIter, collections::HashMap};
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
        let mut M : HashMap<i64, Vec<usize>> = HashMap::new();
        for i in 0..n {
            M.entry(a[i]).or_default().push(i);
        }
        let mut ans = 0 as i64;
        ans = M.entry(1).or_default().len() as i64 * M.entry(2).or_default().len() as i64;
        for x in M.values() {
            let l = x.len() as i64;
            ans += l * (l - 1) / 2;
        }
        println!("{}", ans);
        
    }
}
