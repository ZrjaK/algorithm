#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(unused_must_use)]
#![allow(unused_mut)]

use std::{collections::BTreeMap, io::Read, vec::IntoIter};

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
    let mut a = (0..n).map(|_| scanner.next::<i64>()).collect::<Vec<_>>();
    let mut x = a.clone().into_iter().reduce(|x, y| x ^ y).unwrap();
    if x != 0 {
        println!("-1");
        return;
    }
    let mut M = BTreeMap::<i64, i64>::new();
    for i in a.iter() {
        *M.entry(*i).or_insert(0) += 1;
    }
    for (k, v) in M.iter().rev() {
        if v % 2 == 1 {
            println!("{}", k - 1);
            return;
        }
    }
    println!("0");
}

fn main() {
    let mut scanner = Scanner::new();
    let T = 1;
    // let T = scanner.next();
    for _ in 0..T {
        solve(&mut scanner);
    }
}
