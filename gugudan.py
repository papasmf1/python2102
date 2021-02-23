# gugudan.py 
# Outer(외부 루프)
for x in [2,3,4,5,6]:
    print("--{0}--단".format(x))
    # Inner(내부 루프)
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


#반복 구문(break, continue)
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #다중 라인 주석 처리:  ctrl + /   /*   ...   */
    if i > 5:
        break 
    print("Item:{0}".format(i))

#조건이 맞으면 스킵하도록~~ 
print("===이번에는 continue===")
for i in lst:
    #다중 라인 주석 처리:  ctrl + /   
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

