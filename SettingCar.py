import time
from SettingManage import ParkManage
#一个关于车的类
class Car(ParkManage):
    def __init__(self,car_number,car_owner,car_color,car_model,contract_way):
        super(Car,self).__init__(car_number)
        self.car_number=car_number
        self.car_owner=car_owner
        self.car_color=car_color
        self.car_model=car_model
        self.contract_way=contract_way
        self.balance=100
        self.entrance_time=0
        self.exit_time=0
    def __setitem__(self,key,Value):
        self.__dict__[key]=Value
    def slot_card(self):
        #根据时间计费
        park_time=time.mktime(time.strptime(self.exit_time))-time.mktime(time.strptime(self.entrance_time))
        h=park_time//3600
        m=(park_time-h*3600)//60
        s=park_time-h*3600-m*60
        p_time='%.0f时%.0f分%.0f秒'%(h,m,s)
        consumption=(park_time/3600)*5
        self.balance-=consumption
        print('车牌号为:%s\n停车时长:%s\n本次消费:%.2f元\n卡里余额:%.2f元\n'%(self.car_number,p_time,consumption,self.balance))

    def __str__(self):
        if self.car_model=='0':
            self.car_model='小汽车'
        elif self.car_model=='1':
            self.car_model=='小卡'
        elif self.car_model=='2':
            self.car_model='中卡'
        elif self.car_model=='3':
            self.car_model=='大卡'
        return '%s %s %s %s %s %s'%(self.car_number,self.car_owner,self.car_color,self.car_model,self.contract_way,self.entrance_time)

