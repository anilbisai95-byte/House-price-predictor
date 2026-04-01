'''house_sizes =[1000, 1200, 1500, 1800]
house_prices = [50, 60, 75, 90]

for x,y in zip(house_sizes, house_prices):
    print("Input: ",x, "output: ",y)'''


from sklearn.linear_model import LinearRegression
house_sizes =[[1000], [1200], [1500], [1800]]
house_prices = [4000, 4800, 6000, 7200]

model = LinearRegression()
model.fit(house_sizes, house_prices)

prediction =model.predict([[1700]])
print(prediction)
