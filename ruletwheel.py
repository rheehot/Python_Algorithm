import random

stop_flag = True
game_count = 0
while stop_flag:
    fi = list()
    for _ in range(50):
        fi.append(random.randint(0,100))
    point = random.uniform(0, sum(fi)/len(fi))
    ss = 0
    www=[]
    for i in range(len(fi)):
        ss = ss + fi[i]
        if(point < ss):
            www.append(fi[i])
            if len(www) == 5:
                print(www)
                ss = 0
                www = []
                game_count += 1
                if game_count == 5:
                    stop_flag = False
                break;
