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
        let mut k: usize = scanner.next();
        let mut s = scanner.next::<String>();
        let mut A = Vec::new();
        let mut B = Vec::new();
        for i in 0..n {
            if &s[i..i+1] == "A" {
                A.push(i);
            } else {
                B.push(i);
            }
        }
        if k == B.len() {
            println!("0");
        } else {
            println!("1");
            if k > B.len() {
                k -= B.len();
                println!("{} B", A[k - 1] + 1);
            } else {
                k = B.len() - k;
                println!("{} A", B[k - 1] + 1);
            }
        }
    }
}
