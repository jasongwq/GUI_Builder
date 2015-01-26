#import pprint, pickle
#a1 = 'apple'
#
#output = open('data.pkl', 'wb')
#pickle.dump(a1, output)
#output.close()
#
#pkl_file = open('data.pkl', 'rb')
#data1 = pickle.load(pkl_file)
#pprint.pprint(data1)
#pkl_file.close()
#
#使用pickle模块从文件中重构python对象
output = open('data.pkl', 'wb')
pickle.dump(Win_config, output)
output.close()
pkl_file = open('data.pkl', 'rb')
Win_config = pickle.load(pkl_file)
pprint.pprint(Win_config)
pkl_file.close()

