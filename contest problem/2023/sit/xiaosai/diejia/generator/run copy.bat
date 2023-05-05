py small.py > ./data/small_1.in
py small.py > ./data/small_2.in
py small.py > ./data/small_3.in
py small.py > ./data/small_4.in
py small.py > ./data/small_5.in

py large_hard.py > ./data/large_hard_1.in
py large_hard.py > ./data/large_hard_2.in
py large_hard.py > ./data/large_hard_3.in
py large_hard.py > ./data/large_hard_4.in
py large_hard.py > ./data/large_hard_5.in
py large_hard.py > ./data/large_hard_6.in
py large_hard.py > ./data/large_hard_7.in
py large_hard.py > ./data/large_hard_8.in
py large_hard.py > ./data/large_hard_9.in
py large_hard.py > ./data/large_hard_10.in
py large_hard.py > ./data/large_hard_11.in
py large_hard.py > ./data/large_hard_12.in
py large_hard.py > ./data/large_hard_13.in
py large_hard.py > ./data/large_hard_14.in
py large_hard.py > ./data/large_hard_15.in

g++ -std=c++17 -w -O2 std.cpp

./a.exe < ./data/small_1.in > ./data/small_1.out
./a.exe < ./data/small_2.in > ./data/small_2.out
./a.exe < ./data/small_3.in > ./data/small_3.out
./a.exe < ./data/small_4.in > ./data/small_4.out
./a.exe < ./data/small_5.in > ./data/small_5.out

./a.exe < ./data/large_hard_1.in > ./data/large_hard_1.out
./a.exe < ./data/large_hard_2.in > ./data/large_hard_2.out
./a.exe < ./data/large_hard_3.in > ./data/large_hard_3.out
./a.exe < ./data/large_hard_4.in > ./data/large_hard_4.out
./a.exe < ./data/large_hard_5.in > ./data/large_hard_5.out
./a.exe < ./data/large_hard_6.in > ./data/large_hard_6.out
./a.exe < ./data/large_hard_7.in > ./data/large_hard_7.out
./a.exe < ./data/large_hard_8.in > ./data/large_hard_8.out
./a.exe < ./data/large_hard_9.in > ./data/large_hard_9.out
./a.exe < ./data/large_hard_10.in > ./data/large_hard_10.out
./a.exe < ./data/large_hard_11.in > ./data/large_hard_11.out
./a.exe < ./data/large_hard_12.in > ./data/large_hard_12.out
./a.exe < ./data/large_hard_13.in > ./data/large_hard_13.out
./a.exe < ./data/large_hard_14.in > ./data/large_hard_14.out
./a.exe < ./data/large_hard_15.in > ./data/large_hard_15.out

