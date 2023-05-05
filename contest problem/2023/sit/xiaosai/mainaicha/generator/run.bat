py large.py > ./data/large_1.in
py large.py > ./data/large_2.in
py large.py > ./data/large_3.in

py small.py > ./data/small_1.in
py small.py > ./data/small_2.in
py small.py > ./data/small_3.in
py small.py > ./data/small_4.in
py small.py > ./data/small_5.in

py std.py < ./data/large_1.in > ./data/large_1.out
py std.py < ./data/large_2.in > ./data/large_2.out
py std.py < ./data/large_3.in > ./data/large_3.out

py std.py < ./data/small_1.in > ./data/small_1.out
py std.py < ./data/small_2.in > ./data/small_2.out
py std.py < ./data/small_3.in > ./data/small_3.out
py std.py < ./data/small_4.in > ./data/small_4.out
py std.py < ./data/small_5.in > ./data/small_5.out
