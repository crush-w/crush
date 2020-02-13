import re
dic_num = {
            '零':0,
            '一':1,
            '二':2,
            '三':3,
            '四':4,
            '五':5,
            '六':6,
            '七':7,
            '八':8,
            '九':9,
            '十':10
            }

#分离每一行中的每一个变量
def get_str(s1):
           s2=[]
           s2=s1.split(' ')
           return s2


#通过字典实现数字转化（中文数字——>阿拉伯数字） 
def get_num(number):
           #print(number)
           num = [[],[],[],[]]
           i = 0
           f = 0 #标记负数
           #分离中文数字中的每一个字
           for s in number:
                      num[i] = s
                      i=i+1
           #判断负数
           if num[0] == '负':
                      f = 1
                      del num[0]                  
           result1 = re.match('^[\u4e00-\u9fa5]{2,}$',number)#判断两个字以上
           result2 = re.match('^[\u4e00-\u9fa5]{3,}$',number)#判断三个字以上
           result3 = re.match('^[\u4e00-\u9fa5]{4,}$',number)#判断四个字以上
           if f == 1:
                      if result2 is not None :
                                 if (num[0] == '十') :
                                            n = dic_num[num[0]]+dic_num[num[1]] #-11~-19
                                 elif (num[0] == num[1]) | (result3 is not None):
                                            n = dic_num[num[0]]*10+dic_num[num[2]] #eg:-21、-88
                                 else:
                                            n = dic_num[num[0]]*10 #eg:-20
                      else:
                                 n =  dic_num[num[0]] #-1~-10
                                 
           else:
                      if  result1 is not None :
                                 if (num[0] == '十') :
                                            n = dic_num[num[0]]+dic_num[num[1]] #11~19
                                 elif (num[0] == num[1]) | (result2 is not None):
                                            n = dic_num[num[0]]*10+dic_num[num[2]] #eg:21、99
                                 else:
                                            n = dic_num[num[0]]*10 #eg:20
                      else:
                                 n =  dic_num[number] #0~10
                                 
           #通过标志位，还原负数
           if f == 1:
                      n = -n
           #print(n)
           return n
                    
#判断赋值语句（通过整数，浮点数等变量类型进行识别）                     
def judge_type(ty_pe):
           result = re.match('[整数浮点数]',ty_pe)
           if  result is not None:
                      return 1
           else:
                      return 0
           
#变量类型转化 
def get_type(ty_pe,x):
           if ty_pe == '整数':
                      x = int(x)
           elif ty_pe == '浮点数':
                      x = float(x)
           return x

#识别赋值语句，实现汉字转数字、类型转化
def get_def(arr):
           f = 0
           for a in arr:
                      #print(a) 
                      if  judge_type(a) == 1:
                                 f = judge_type(a)
                                 ty_pe = a
                      if  f == 1:
                                 result = re.match('[负零一二三四五六七八九十]',a)
                                 #print(result)
                                 if result is not None:
                                            x = get_num(a) #汉字转数字
                                            x = get_type(ty_pe,x)  #类型转化
                                            return x
                      else:
                                 return None

#算术运算（仅限加减）                        
def get_lastnum(n,arr):
           for a in arr:
                      result = re.match('[零一二三四五六七八九十]',a)
                      if result is not None:
                                 num = get_num(a) #汉字转数字
           for a in arr:
                      if a == '增加':
                                 n = n+num
                      elif a == '减少':
                                 n = n-num
           return n;


#通过字典实现数字转化数字转化（阿拉伯数字——>中文）
def print_num(n):
           #print(n)
           f=0 #判断正负的标志位
           #当n<0,改为正数处理
           if n<0:
                      n = -n
                      f = 1
           if n >10:
                      n1 = int(n/10)  #得十位
                      n2 = n%10  #得个位
                      for num in dic_num:
                                 if (n1 == dic_num[num]) & (n2 == dic_num[num]):
                                            s1 = num
                                            s2 = num
                                 elif n1 == dic_num[num]:
                                            s1 = num
                                 elif n2 == dic_num[num]: 
                                            s2 = num
                      if n1 == 1:
                                 key = '十'+s2 #10~20
                      elif n2 == 0:
                                 key = s1+'十' #拼接数字 20、30...
                      else:
                                 key = s1+'十'+s2 #拼接数字 21、31...
                      
           else:
                      for num in dic_num:
                                 if n == dic_num[num]:
                                            key = num
           if f == 1:
                      key = '负'+key
           return key

#一个变量：返回指定字符串
def compare1(arr,n):
           word = [[],[]]
           i=0
           #取得判断数
           for a in arr:
                      result = re.match('[零一二三四五六七八九十]',a)
                      if result is not None:
                                 num = get_num(a) #汉字转数字

           for a in arr:
                      result1 = re.match('“(.*?)”',a)
                      if result1 is not None:
                                 a1=a.strip('“”') #去双引号
                                 word[i]=a1
                                 i=i+1
           for a in arr:
                      if a == '大于':
                                 if n > num:
                                            print(word[0])
                                 else:
                                            print(word[1])
                      elif a == '小于':
                                 if n < num:
                                            print(word[0])
                                 else:
                                            print(word[1])
                                                                
#两个变量、实现比较，返回算术运算后的结果
def compare2(arr,n,x):  #n:比较数  x：改变数
           num = [[],[]]
           i=0
           f=0
           for a in arr:
                      result = re.match('[零一二三四五六七八九十]',a)
                      if result is not None:
                                 num[i] = get_num(a) #汉字转数字
                                 i=i+1
           for a in arr:
                      if a == '大于':
                                 if n > num[0]:
                                            f = 1
           for a in arr:
                      if f == 1:
                                 if a == '增加':
                                            n = x + num[1]
                                            return n
                                 
                                 elif a == '减少':
                                            n = x - num[1]
                                            return n
                      else:
                                 return None
    
def main():
           pattern1 = '等于'
           pattern2 = '^看看'
           pattern3 = '^如果'
           pattern4 = '无'
           i = 0
           while(1):
                      s = input()
                      arr = get_str(s)#分割
                      res1 = re.search(pattern1,s) #赋值语句
                      res2 = re.search(pattern2,s) #输出语句
                      res3 = re.search(pattern3,s) #判断语句
                      res4 = re.search(pattern4,s) #判断语句（两个变量）
                      if res1 is not None:
                                 x = get_def(arr)
                                 i = i+1
                                 #print(x)
                                 if i == 2: #两个变量
                                            a[1] = arr[1]
                                            n[1] = x
                                            i = 0
                                            #print(n[1])
                                 else:
                                            a[0] = arr[1]
                                            n[0] = x
                                            #print(n[0])
                      if arr[0] == a[0]:
                                 n[0] = get_lastnum(n[0],arr)
                      elif arr[0] == a[1]:
                                 n[1] = get_lastnum(n[1],arr)
                                 
                      if res2 != None:
                                 if arr[1] == a[0]:
                                            print(print_num(n[0]))
                                 elif arr[1] == a[1]:
                                            print(print_num(n[1]))

                      if (res3 != None) & (res4 != None):
                                 if (arr[1] == a[0]) & (arr[5] == a[0]):
                                            n[0] = compare2(arr,n[0],n[0])
                                            #print(print_num(n[0]))
                                 if (arr[1] == a[0]) & (arr[5] == a[1]):
                                            n[1] = compare2(arr,n[0],n[1])
                                            #print(print_num(n[1]))
                                 if (arr[1] == a[1]) & (arr[5] == a[0]):
                                            n[0] = compare2(arr,n[1],n[0])
                                            #print(print_num(n[0]))
                                 if (arr[1] == a[1]) & (arr[5] == a[1]):
                                            n[1] = compare2(arr,n[1],n[1])
                                            #print(print_num(n[1]))
                      else:
                                 compare1(arr,n[0])
                                                                                                                                                                           
if __name__=='__main__':
           a = ['','']
           n = ['','']
           main()
