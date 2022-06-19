from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class data :
    def __init__(self):
        self.list = []

    def setlist(self,leng):
        for i in range(leng):
            try:
                self.list.append([self.list[self.list.__len__()-1][0] + (i+1)**4])
            except IndexError:
                self.list.append([1])
    
    def getlist(self):
        return self.list
    
    def getlist_(self):
        return [i[0] for i in self.list]
    

rawdata = data()
rawdata.setlist(9000)
y = rawdata.getlist()
x = [[i+1] for i in range(9000)]
x_train = x[:8000]
x_test = x[8000:]

y_train = y[:8000]
y_test = y[8000:]

poly = PolynomialFeatures(degree=5, include_bias=False)

x_train_ = poly.fit_transform(x_train)
x_test_ = poly.fit_transform(x_test)

print('모델 훈련중')
model = LinearRegression()
model.fit(x_train_,y_train)
print("정확도 : ",model.score(x_test_,y_test))
    

ans = ''
while True:
    ans = input('>>>')
    if ans == "exit" or ans == "ㄷ턋" :
        print('프로그램 종료')
        break
    poly = PolynomialFeatures(degree=5, include_bias=False)
    x_pre = poly.fit_transform([[int(ans)]])
    print(x_pre)
    print(model.predict(x_pre)[0][0])