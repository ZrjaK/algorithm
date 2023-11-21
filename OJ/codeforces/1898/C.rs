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
        let mut m: usize = scanner.next();
        let mut k: usize = scanner.next();
        if k < n - 1 + m - 1 || (k + n + m) % 2 == 1 {
            println!("NO");
            continue;
        }
        println!("YES");
        for i in 0..n {
            let mut X = String::new();
            for j in 0..m - 1 {
                let mut x = (i + j) % 2;
                if i == 0 && j == 0 {
                    x ^= 1;
                }
                X += if x == 1 {"B "} else {"R "};
            }
            X.pop();
            println!("{}", X);
        }
        for i in 0..n - 1 {
            let mut X = String::new();
            for j in 0..m {
                let mut x = (i + j) % 2;
                if i == 0 && j == 1 {
                    x ^= 1;
                }
                X += if x == 1 {"B "} else {"R "};
                
            }
            X.pop();
            println!("{}", X);
        }
    }
}
