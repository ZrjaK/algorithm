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
    let mut f: Vec<Vec<bool>> = vec![vec![false; 110]; 110];
    for m in 1..101 {
        for a in 1..101 {
            let mut x = 0;
            let mut s = 0;
            for b in 1..101 {
                if a + b <= m && (a % b == 0 || b % a == 0) {
                    s += b;
                    x += 1;
                }
            }
            f[m][a] = s > x * a;
        }
    }
    for _ in 0..T {
        let mut m: usize = scanner.next();
        let mut a: usize = scanner.next();
        if f[m][a] {
            println!("YES");
        } else {
            println!("NO");
        }
        
    }
}
