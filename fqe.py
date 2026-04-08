from bigMac import BigMac
import matplotlib.pyplot as plt


lis_1 = BigMac("dollar_price", "name").dollar_pr





value_coun = lis_1.keys()
value_pr = lis_1.values()

value_pr = value_pr.sort()



plt.barh(value_coun, value_pr) #https://pythonru.com/biblioteki/tipy-grafikov-v-matplotlib-plt3
plt.show()