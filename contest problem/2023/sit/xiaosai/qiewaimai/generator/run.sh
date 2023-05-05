py large_1.py > ./data/large_1.in
py large_2.py > ./data/large_2.in
py large_3.py > ./data/large_3.in
py large_4.py > ./data/large_4.in
py large_5.py > ./data/large_5.in
py large_6.py > ./data/large_6.in
py large_7.py > ./data/large_7.in
py large_8.py > ./data/large_8.in

py small_1.py > ./data/small_1.in
py small_2.py > ./data/small_2.in
py small_3.py > ./data/small_3.in

py std.py < ./data/large_1.in > ./data/large_1.out
py std.py < ./data/large_2.in > ./data/large_2.out
py std.py < ./data/large_3.in > ./data/large_3.out
py std.py < ./data/large_4.in > ./data/large_4.out
py std.py < ./data/large_5.in > ./data/large_5.out
py std.py < ./data/large_6.in > ./data/large_6.out
py std.py < ./data/large_7.in > ./data/large_7.out
py std.py < ./data/large_8.in > ./data/large_8.out

py std.py < ./data/small_1.in > ./data/small_1.out
py std.py < ./data/small_2.in > ./data/small_2.out
py std.py < ./data/small_3.in > ./data/small_3.out
