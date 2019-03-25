#课堂练习：生成扑克牌
def poker():
    color = ['梅花','方块','黑桃','红心']
    num = list(range(2,11))
    num.extend('JQKA')
    return [(x,y)for x in color for y in num]

print(poker()) 


#课堂练习：魔塔游戏
import time,random
while True:

    n = 1 #局数
    win = 0
    lose = 0
    for rand in range(3):
        a = random.randint(100,150)
        b = random.randint(30,50)
        aa = random.randint(100,150)
        bb = random.randint(30,50)

        print('玩家血量为 {} 玩家攻击力为 {}'.format(a,b))
        print('怪物血量为 {} 怪物攻击力为 {}'.format(aa,bb))
        print('------------------------------')
        time.sleep(1)
        c = 1
        print('现在是第 %d 局'%(n))
        for i in range(3):        
            aa = aa - b
            a = a - bb
            print('发动第%d轮攻击'%(c))
            print('你攻击了怪兽，【怪兽】血量：'+ str(aa))
            print('怪兽攻击了你，【玩家】血量：'+str(a))
            print('------------------------------')
            c += 1
            time.sleep(1)
            if a < 0 or aa < 0:
                break

        print('战斗结束')
        if a > aa:
            print('怪物死了，你获胜了')
            win += 1
        elif a < aa :
            print('你失败了，怪物获胜')
            lose += 1
        else:
            print('平局，跟怪物握个手吧')
        n +=1 
    if win > lose:
        print('三局两胜，你赢了')
    elif win == lose:
        print('打成平手')
    else:
        print('三局两败，你输了') 
    a = input('要再来一局吗？')
    if a != '要':
        break    

#课堂练习：帮老师算分数
import numpy as np

list1 =  [91, 95, 97, 99]  
list2 =  [92, 93, 96, 98]
list1.extend(list2)
average = np.mean(list1)
print (list1)
print('成绩排序为{}'.format(sorted(list1)))
print('平均分为{}'.format(average))
print('低于平均分的分数有：')
for i in list1:
    if i < average:
        print(i,end = '  ')


#课堂练习：电影问答（优化版）
movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('你想查询哪个演员？')


a = False
for i in movies:
        if actor in movies[i]:
                print('{}出演了{}'.format(actor,i))
                a = True
if a == False:
        print('没有查询到该演员的信息')



#实例1：数字组合
a = ['1','2','3','4']
list1 = []
for i in a:
    for o in a:
        for u in a:
            if (i+u+o) not in list1 and i !=o and o!=u and u !=i:
                list1.append(i+u+o)
print(list1)
print(len(list1))


#剪刀石头布
import random
punch = ['剪刀','布','石头']
player = input('请出拳')
computer = random.choice(punch)
if player in punch:
    if player == computer:
        print('平局')
    elif player == punch[punch.index(computer)-1]:
        print('你输了')
    else:
        print('你赢了')
else:
    print('只可以出剪刀/石头/布')


#练习：贴心计算器
try:
    a = int(input('请输入除数'))
    b = int(input('请输入被除数'))
    c= b/a
    print(c)
except ZeroDivisionError:
    print('0不能被整除')
except ValueError:
    print('请输入整数')


#绩效计算器
worker = ['a','b','c','d','e']
class kip_excel():
    @classmethod
    def entry(cls):
        cls.name = input('请输入员工姓名')
        cls.kpi = int(input('请输入员工kpi（0-100）'))
    
    @classmethod
    def level(cls):
        if cls.name not in worker:
            print('这个人不在本公司上班')
        else:
            if cls.kpi > 90:
                print('{}是明星员工'.format(cls.name))
            elif cls.kpi <=90 and cls.kpi> 80:
                print('{}是优秀员工'.format(cls.name))
            else:
                print('{}今年没评上，继续努力！'.format(cls.name))

kip_excel.entry()
kip_excel.level()


#日程表
class calender():
    cal = {'get up':'8:00'}
    @classmethod
    def edit(cls):
        cls.time=input('请输入时间')
        cls.things = input('请输入要完成的事件')
        cls.cal[cls.time] =cls.things
        print(cls.cal)
    @classmethod
    def search(cls):
        a = input('请输入要查询的事件')
        if a in cls.cal:
            for i in cls.cal:
                if a == i:
                    print('{}的安排时间是{}'.format(i,cls.cal[i]))
        else:
            print('您今天没有安排这件事喔')

    @classmethod
    def finish(cls):
        print(cls.cal)
        fini= input('您今天完成了什么事？')
        if fini not in cls.cal:
            print('今天的日程表没有这个安排，你额外完成了工作噢')
        else:
            for i in list(cls.cal):
                if fini == i:
                    del cls.cal[i]
        print('最新的日程表{}'.format(cls.cal))

calender.finish()



#问卷调查-单个问题
class question():
    def __init__(self,ques):
        self.ques = ques
        self.list = []

    def show(self):
        print(self.ques)
    
    def store(self,new_ans):
        self.list.append(new_ans)



food = question('你最喜欢什么食物？')
food.show()
while True:
    new_ans= input('请输入答案，按q退出')
    if new_ans =='q':
        break
    else:
        food.store(new_ans)

print(food.list)

#问卷调查升级版-姓名与籍贯
class question():
    def __init__(self,ques):
        self.ques = ques
        self.list = []

    def show(self):
        print(self.ques)
    
    def store(self,new_ans):
        self.list.append(new_ans)



class new_survey(question):
    def __init__(self,ques):
        self.ques = ques
        self.list = {}

    def store(self,name,place):
        self.list[name]=place


new = new_survey('你是谁，来自哪里？')
new.show()
while True:
    name= input('请输入姓名，按q退出')
    if name =='q':
        break
    else:
        place= input('请输入您的籍贯，按q退出')
        if place =='q':
            break
        else:
            new.store(name,place)

print(new.list)

#那个毛球来了
class man():
    def __init__(self,name):
        self.name = name

    def show(self):
        print('那个叫{}的男人走过来了'.format(self.name))

class man_back(man):
    def back(self):
        print('那个叫{}的男人走了，留下了他的背影'.format(self.name))

the_one = man('基多')
the_one.show()
second = man_back('毛球')
second.show()
second.back()

#小游戏最终版
import random
import time

class born():#生成普通角色
    def __init__(self,name = '普通角色'):
        self.name = name
        self.life = random.randint(50,100)
        self.attack = random.randint(100,150)

class killer(born):#生成三个不同属性的角色
    def __init__(self,name ='兰陵王'):
        born.__init__(self,name) 
        self.life = self.life * 3
        self.attack = self.attack * 5

    def buff(self,opponent,words1,words2):#opponent为敌手（实例）
        if opponent.name == '后羿':
            self.attack = self.attack * 1.5
            print('{}兰陵王对{}后羿说：小脆皮别跑'.format(words1,words2))

class dps(born):
    def __init__(self,name ='后羿'):
        born.__init__(self,name) 
        self.life = self.life * 4
        self.attack = self.attack * 4

    def buff(self,opponent,words1,words2):#opponent为敌手（实例）
        if opponent.name == '项羽':
            self.attack = self.attack * 2
            print('{}后羿对{}项羽说：虽然你皮厚但是我削得快'.format(words1,words2))

class t(born):
    def __init__(self,name ='项羽'):
        born.__init__(self,name) 
        self.life = self.life * 5
        self.attack = self.attack * 2

    def buff(self,opponent,words1,words2):#opponent为敌手（实例）
        if opponent.name == '兰陵王':
            self.attack = self.attack * 1.5
            print('{}项羽对{}兰陵王说：爸爸血厚不怕你打'.format(words1,words2))



class game():#一个游戏类
    def __init__(self):
        self.plays = []
        self.enemies = []
        self.score = 0
        self.rand = 0
        self.start()
        self.born_role()
        self.show_role()
        self.team()
        self.chose_role()
        self.pk()
        self.show_result()

    def start(self):
        print('==============游戏开始==============')
        print('欢迎来到瞎玩竞技场，我没什么欢迎的话要说')
        time.sleep(0.5)
        print('既然来了你就试一试这个游戏吧，你可以得到三个角色并决定出场顺序')
        time.sleep(0.5)
        input('点击回车键继续')

    def born_role(self):#随机生成两个对战列表
        for a in range(3):
            self.plays.append(random.choice([killer(),dps(),t()]))
            self.enemies.append(random.choice([killer(),dps(),t()]))
        

    def team(self):#触发团队技能
        if self.plays[0].name != self.plays[1].name and self.plays[0].name != self.plays[2].name and self.plays[1].name != self.plays[2].name:
            print('所有角色属性不同，触发效果【各有所长】，所有角色攻击增加25%')
            for i in range(3):
                self.plays[i].attack = self.plays[i].attack *1.25
            self.show_role()
        if self.plays[0].name == self.plays[1].name and self.plays[0].name == self.plays[2].name:
            print('所有角色属性相同，触发效果【同心协力】，所有角色生命增加25%')
            for i in range(3):
                self.plays[i].life = self.plays[i].life *1.25
            self.show_role()

    def show_role(self):
        print('==============玩家角色==============')
        for i in range(3):
            print('【{}】 血量：{} 攻击：{}'.format(self.plays[i].name,self.plays[i].life,self.plays[i].attack))
            time.sleep(0.5)
        print('==============敌方角色：==============')
        for i in range(3):
            print('【{}】 血量：{} 攻击：{}'.format(self.enemies[i].name,self.enemies[i].life,self.enemies[i].attack))
            time.sleep(0.5)
        print('----------------------------')
        input('请按回车键继续')

    def chose_role(self):
        global order_list
        player_order = {}
        order_list = []
        order = []
        c = 0
        while True:
            write = input('请输入{}的出场次序'.format(self.plays[c].name))
            if write in order:
                print('请不要输入相同的序号')
            elif write != '1' and write != '2' and write != '3':
                print('请输入正确的序号，如1、2、3')
            else:
                a = int(write)- 1
                player_order[a] = self.plays[c]
                c += 1
                order.append(write)
            if len(order) == 3:
                break
                
        for i in range(3):
            order_list.append(player_order[i])
        print('玩家的出战顺序是\n{}\n{}\n{}'.format(order_list[0].name,order_list[1].name,order_list[2].name))
        time.sleep(0.5)
        print('敌人的出战顺序是\n{}\n{}\n{}'.format(self.enemies[0].name,self.enemies[1].name,self.enemies[2].name))
        input('请按回车键继续')

    def pk(self):#三局pk
        for i in range(3):
            player = order_list[i].name
            enemy = self.enemies[i].name
            order_list[i].buff(self.enemies[i],'我方','敌方')
            self.enemies[i].buff(order_list[i],'敌方','我方')
            player_life = order_list[i].life
            player_attack = order_list[i].attack
            enemy_life = self.enemies[i].life
            enemy_attack = self.enemies[i].attack
            
            print('我方【{}】血量: {}  攻击力: {}'.format(player,player_life,player_attack))
            print('敌方【{}】血量: {}  攻击力: {}'.format(enemy,enemy_life,enemy_attack))
            print('------------------------------')
            time.sleep(0.5)
            while player_life > 0 and enemy_life > 0:
                player_life -= enemy_attack
                enemy_life -= player_attack
                print('你向敌方发起了一次攻击 【{}】血量：{}'.format(enemy,enemy_life))
                print('敌方向你发起了一次攻击【{}】血量：{}'.format(player,player_life))
            if player_life> 0:
                print('本局【{}】获胜'.format(player))
                self.score+= 1
            elif enemy_life > 0:
                print('本局【{}】获胜'.format(enemy))
                self.score-= 1
            else:
                print('本局平局')
            print('------------------------------')
            self.rand += 1

    def show_result(self):
        if self.score > 0:
            print('你赢了')
        elif self.score == 0:
            print('平局')
        else:
            print('你输了')

game =game()
