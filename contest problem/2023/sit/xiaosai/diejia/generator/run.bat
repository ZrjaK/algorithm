py small.py > ./data/small_1.in
py small.py > ./data/small_2.in
py small.py > ./data/small_3.in
py small.py > ./data/small_4.in
py small.py > ./data/small_5.in

py large_easy.py > ./data/large_easy_1.in
py large_easy.py > ./data/large_easy_2.in
py large_easy.py > ./data/large_easy_3.in
py large_easy.py > ./data/large_easy_4.in
py large_easy.py > ./data/large_easy_5.in

g++ -std=c++17 -w -O2 std.cpp

./a.exe < ./data/small_1.in > ./data/small_1.out
./a.exe < ./data/small_2.in > ./data/small_2.out
./a.exe < ./data/small_3.in > ./data/small_3.out
./a.exe < ./data/small_4.in > ./data/small_4.out
./a.exe < ./data/small_5.in > ./data/small_5.out

./a.exe < ./data/large_easy_1.in > ./data/large_easy_1.out
./a.exe < ./data/large_easy_2.in > ./data/large_easy_2.out
./a.exe < ./data/large_easy_3.in > ./data/large_easy_3.out
./a.exe < ./data/large_easy_4.in > ./data/large_easy_4.out
./a.exe < ./data/large_easy_5.in > ./data/large_easy_5.out
