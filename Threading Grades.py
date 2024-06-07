import time,threading as th
def grad(scores):
    time.sleep(1)
    a,b,c,d,e=scores
    f= (a+b+c+d+e)/5
    if f>=18:
        print(f"Grade is A with average of {f} out of 20\nTotal is {a+b+c+d+e} out of 100")
    elif f>=15:
        print(f"Grade is B with average of {f} out of 20\nTotal is {a+b+c+d+e} out of 100")
    elif f>=12:
        print(f"Grade is C with average of {f} out of 20\nTotal is {a+b+c+d+e} out of 100")
    elif f>=9:
        print(f"Grade is D with average of {f} out of 20\nTotal is {a+b+c+d+e} out of 100")
    elif f<6:
        print(f"Grade is E with average of {f} out of 20\nTotal is {a+b+c+d+e} out of 100")
    return
x=[[19,18,17,13,19],[15,18,17,19,19],[19,10,17,13,19],[15,19,17,19,19],[19,18,17,19,19],[15,18,9,19,19],[17,18,17,13,19],[15,18,16,19,19]]
t1=time.perf_counter()
threads=[]
for y in x:
    t=th.Thread(target=grad,args=(y,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
t2=time.perf_counter()
print(f'Finished in {t2-t1} seconds')