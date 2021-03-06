library(fpp2)
data = read.csv('C:/Users/chomjung/OneDrive - �������б�/�����׽�Ʈ2020/1��_����_������/1��_����_�ֱ�_��Ÿ��.csv', stringsAsFactors =TRUE, header = TRUE, encoding="UTF-8")
NCdata= subset(data, ���ڵ�=='NC')
SKdata= subset(data, ���ڵ�=='SK')
KTdata= subset(data, ���ڵ�=='KT')
OBdata= subset(data, ���ڵ�=='OB')
WOdata= subset(data, ���ڵ�=='WO')
HHdata= subset(data, ���ڵ�=='HH')
SSdata= subset(data, ���ڵ�=='SS')
LGdata= subset(data, ���ڵ�=='LG')
HTdata= subset(data, ���ڵ�=='HT')
LTdata= subset(data, ���ڵ�=='LT')

# NC
NCdata <- ts(NCdata$�ܷ�,start = 2016,end = 2019,frequency = 20)
NCdata = stl(NCdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(NCdata)
ft = max(0,1-var(NCdata$time.series[,3])/(var(NCdata$time.series[,2]+NCdata$time.series[,3]))); ft
fs = max(0,1-var(NCdata$time.series[,3])/(var(NCdata$time.series[,1]+NCdata$time.series[,3]))); fs

# SK
SKdata <- ts(SKdata$2��Ÿ,start = 2016,end = 2019,frequency = 20)
SKdata = stl(SKdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(SKdata)
ft = max(0,1-var(SKdata$time.series[,3])/(var(SKdata$time.series[,2]+SKdata$time.series[,3]))); ft
fs = max(0,1-var(SKdata$time.series[,3])/(var(SKdata$time.series[,1]+SKdata$time.series[,3]))); fs

# KT
KTdata <- ts(KTdata$��Ÿ,start = 2016,end = 2019,frequency = 20)
KTdata = stl(KTdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(KTdata)
ft = max(0,1-var(KTdata$time.series[,3])/(var(KTdata$time.series[,2]+KTdata$time.series[,3]))); ft
fs = max(0,1-var(KTdata$time.series[,3])/(var(KTdata$time.series[,1]+KTdata$time.series[,3]))); fs

# OB
OBdata <- ts(OBdata$��Ÿ,start = 2016,end = 2019,frequency = 20)
OBdata = stl(OBdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(OBdata)
ft = max(0,1-var(OBdata$time.series[,3])/(var(OBdata$time.series[,2]+OBdata$time.series[,3]))); ft
fs = max(0,1-var(OBdata$time.series[,3])/(var(OBdata$time.series[,1]+OBdata$time.series[,3]))); fs

# WO
WOdata <- ts(WOdata$��Ÿ,start = 2016,end = 2019,frequency = 20)
WOdata = stl(WOdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(WOdata)
ft = max(0,1-var(WOdata$time.series[,3])/(var(WOdata$time.series[,2]+WOdata$time.series[,3]))); ft
fs = max(0,1-var(WOdata$time.series[,3])/(var(WOdata$time.series[,1]+WOdata$time.series[,3]))); fs

# HH
HHdata <- ts(HHdata$��Ÿ,start = 2016,end = 2019,frequency = 20)
HHdata = stl(HHdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(HHdata)
ft = max(0,1-var(HHdata$time.series[,3])/(var(HHdata$time.series[,2]+HHdata$time.series[,3]))); ft
fs = max(0,1-var(HHdata$time.series[,3])/(var(HHdata$time.series[,1]+HHdata$time.series[,3]))); fs

# SS
SSdata <- ts(SSdata$������Ÿ��,start = 2016,end = 2019,frequency = 20)
SSdata = stl(SSdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(SSdata)
ft = max(0,1-var(SSdata$time.series[,3])/(var(SSdata$time.series[,2]+SSdata$time.series[,3]))); ft
fs = max(0,1-var(SSdata$time.series[,3])/(var(SSdata$time.series[,1]+SSdata$time.series[,3]))); fs

# LG
LGdata <- ts(LGdata$������Ÿ��,start = 2016,end = 2019,frequency = 20)
LGdata = stl(LGdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(LGdata)
ft = max(0,1-var(LGdata$time.series[,3])/(var(LGdata$time.series[,2]+LGdata$time.series[,3]))); ft
fs = max(0,1-var(LGdata$time.series[,3])/(var(LGdata$time.series[,1]+LGdata$time.series[,3]))); fs

# HT
HTdata <- ts(HTdata$������Ÿ��,start = 2016,end = 2019,frequency = 20)
HTdata = stl(HTdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(HTdata)
ft = max(0,1-var(HTdata$time.series[,3])/(var(HTdata$time.series[,2]+HTdata$time.series[,3]))); ft
fs = max(0,1-var(HTdata$time.series[,3])/(var(HTdata$time.series[,1]+HTdata$time.series[,3]))); fs

# LT
LTdata <- ts(LTdata$������Ÿ��,start = 2016,end = 2019,frequency = 20)
LTdata = stl(LTdata, t.window=13, s.window="periodic", robust=TRUE)
autoplot(LTdata)
ft = max(0,1-var(LTdata$time.series[,3])/(var(LTdata$time.series[,2]+LTdata$time.series[,3]))); ft
fs = max(0,1-var(LTdata$time.series[,3])/(var(LTdata$time.series[,1]+LTdata$time.series[,3]))); fs

