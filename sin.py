import numpy as np
import math
import torch
from torch import nn, optim
import  matplotlib.pyplot as plt 
modelname  = 'model/lstmfunction'
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
datainterval=10
def load(num):
    x=range(num)
    #y=3sinx+5cos5x+6
    y=[float(3*math.sin(t)+ math.cos(5*t)+np.random.randn(1,1)+6) for t in x]#每个数据加上一个标准正态随机波动
    return np.array(y,dtype=np.float32)

class lstm(nn.Module):
    def __init__(self, input_size , hidden_size , output_size , num_layer,bidirect =1,dropout=0.1 ):
        super(lstm, self).__init__()
        self.hiddensize= hidden_size
        self.bidirectional=bidirect
        self.layer1 = nn.LSTM(input_size, hidden_size, num_layer ,bidirectional=False if bidirect==1 else True )
        self.Dropped = nn.Dropout(dropout)
        self.Tanh = nn.Tanh()
        self.layer2 = nn.Linear(hidden_size*bidirect, output_size)
        self.BN=nn.BatchNorm1d(datainterval)

    def forward(self, x):
        #Batch Normalize:归一化处理：防止梯度爆炸或消失
        input=self.BN(x)
        #转换成batch*seqlen*inputsize格式
        input = input.view(-1, datainterval, 1)
        # 转换成seqlen*batch*inputsize格式
        x = torch.transpose(input, 0, 1)
        out,(hidden,_) = self.layer1(x)
        #取每个序列的最后一个输出
        out = out[-1, :, :]
        out=out.view(-1, self.hiddensize*self.bidirectional)
        out= self.Dropped (out)
        out = self.layer2(out)


        return out

def create_dataset(num,trainfactor, interval ):
    dataset = load(num)
    dataX, dataY = [], []
    for i in range(len(dataset) - interval):
        a = dataset[i:(i + interval)]
        dataX.append(a)
        dataY.append(dataset[i + interval])
    X,Y=np.array(dataX), np.array(dataY)
    train_size = int( X.shape[0]  * trainfactor)
    train_X, train_Y, test_X, test_Y =  X[:train_size],  Y[:train_size],  X[train_size:],  Y[train_size:]


    train_X = train_X.reshape(-1,  datainterval  )
    train_Y = train_Y.reshape(-1, 1 )
    test_X = test_X.reshape(-1,  datainterval  )
    test_Y = test_Y.reshape(-1, 1 )

    train_x =torch.from_numpy(train_X)
    train_y = torch.from_numpy(train_Y)
    test_x = torch.from_numpy(test_X)
    test_y = torch.from_numpy(test_Y)

    return train_x, train_y, test_x, test_y

def train(train_x, train_y):
    model = lstm(1, 200, 1, 2)
    model.train()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
    iternum=5000
    for e in range(iternum):
        # 前向传播
        out = model(train_x)
        loss = criterion(out, train_y)
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (e + 1) % 1000 == 0:
            torch.save(model, modelname )


        if (e + 1) % 1000 == 0:  # 每 100 次输出结果
            print('迭代数: {}, 损失值: {:.6f}'.format(e + 1, loss.data.item()/train_x.shape[0])  )
    print('\r')


def test(num,trainfactor=0.8):
    model = torch.load(modelname)
    model.eval()
    dataset = load(num)
    train_size = int(dataset.__len__() * trainfactor)
    dataset=dataset[train_size:]
    startnum=datainterval
    predictnum = 50
    x=range(startnum,startnum+predictnum)
    y=dataset[startnum:startnum+predictnum]
    y_=[]
    #取得初始10个数据来预测接下来50个样本点
    data=[x for x in dataset[:datainterval]]
    for i in range(0,predictnum):
        seed = np.array(data[i:i+datainterval],dtype=np.float32)
        seed=seed.reshape(-1,  datainterval )
        p=model(torch.from_numpy(seed))
        y_.append(p.item())
        data.append(p.item())

    plt.plot(x, y, color='blue')
    plt.plot(x, y_, color='red')
    plt.grid()
    plt.show()

if __name__=='__main__':
    runtest = True
    if (runtest):
        test(2000)
    else:
        train_X, train_Y, test_X, test_Y = create_dataset(500, 0.8, datainterval)
        train(train_X, train_Y)