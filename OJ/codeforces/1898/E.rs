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
    let mut s = scanner.next_string();
    let mut t = scanner.next_string();
    let mut pos = vec![vec![0; 0]; 26];
    for (i, c) in s.chars().enumerate() {
        pos[c as usize - 97].push(i);
    }
    for i in 0..26 {
        pos[i].reverse();
    }
    for (i, c) in t.chars().enumerate() {
        let x = c as usize - 97;
        if pos[x].is_empty() {
            println!("NO");
            return;
        }
        let p = pos[x].pop().unwrap();
        for j in 0..x {
            while !pos[j].is_empty() && pos[j].last().unwrap() < &p {
                pos[j].pop();
            }
        }
    }
    println!("YES");
}

fn main() {
    let mut scanner = Scanner::new();
    let T = 1;
    let T = scanner.next();
    for _ in 0..T {
        solve(&mut scanner);
    }
}
