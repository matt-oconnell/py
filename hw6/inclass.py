arr = [1,2,3,4,5]

# 6.1
final = map(lambda x: x * 2, arr)
final2 = [x * 2 for x in arr]
print final
print final2

#6.2
final = [x for x in arr if x > 2]
final2 = filter(lambda x: x > 2, arr)
print final
print final2

#6.3
final = sum(arr)
final2 = reduce(lambda x, y: x + y, arr)
print final
print final2

#6.4
final = reduce(lambda a, x: a / x,
                # reduce to [sum, count]
                reduce(lambda a, x: [a[0] + x, a[1] + 1], arr, [0, 0]),
               )
print final

#6.5
final = reduce(lambda a, x: a * x, arr)
print final

#6.11
wanted_year = '1981'

file_lines = open('F-F_Research_Data_Factors_daily.txt').readlines()
wanted_lines = file_lines[6:-2]


def market_rf(accum, line):
    if wanted_year == line[0:4]:
        items = line.split()
        return float(accum) + float(items[1])
    return accum

print '----------'
print reduce(market_rf, wanted_lines, 0.0)

print
print '----------'



#6.14
def find_yield(arr):
    for num in arr:
        yield num * 2

for entry in find_yield(arr):
    print entry


assert 1 == 1