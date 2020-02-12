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
           try:
                      i = 0
                      pattern = '^看看\s'
                      pattern2 = '\s等于\s'
                      s1 = input()#输入
                      arr1 = get_str(s1)#分割
                      x1=get_def(arr1)#调用函数判断赋值语句，并存储  
                      
                      s2 = input()
                      arr2 = get_str(s2)
                      x2=get_def(arr2)
                      if re.match(pattern,s2) is not None:
                                 if arr2[1] == arr1[1]:
                                            print(arr1[3])
                                 else:
                                            print("名字有误")

                      s3 = input()
                      arr3 = get_str(s3)
                      x3=get_def(arr3)
                      if re.match(pattern,s3) is not None:
                                 if arr2[1] == arr1[1]:
                                            n = get_lastnum(x1,arr2)
                                            print(print_num(n))
                                 else:
                                            print("名字有误")
                                            
                                 if re.match(pattern2,s2) is not None:
                                            if arr1[1] == arr3[1]:
                                                       print(arr1[3])
                                            elif arr2[1] == arr3[1]:
                                                       print(arr2[3])                   
             
                      s4 = input()
                      arr4 = get_str(s4)
                      x4=get_def(arr4)
                      
                      s5 = input()
                      arr5 = get_str(s5)
                      x5=get_def(arr5)       
                     
                      #判断有几个变量
                      for x in (x1,x2):
                                 if x is not None:
                                            i = i+1
                      #一个变量
                      if i == 1:
                                 #运算
                                 n = get_lastnum(x1,arr2)
                                 n = get_lastnum(n,arr3)
                                 #输出
                                 if re.match(pattern,s4) is not None:
                                            print(print_num(n))
                                            compare1(arr5,n)
                                 elif re.match(pattern,s5) is not None:
                                            compare1(arr4,n)
                                            print(print_num(n))                           
                                            
                      #两个变量
                      elif i == 2:
                                 #运算，识别是变量1改变,还是变量2改变，后进行比较输出输出
                                 if arr3[0] == arr1[1]:
                                            n = get_lastnum(x1,arr3)
                                            if (arr4[1] == arr1[1]) & (arr4[5] == arr1[1]):
                                                       n1 = compare2(arr4,n,n)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr1[1]) & (arr4[5] == arr2[1]):
                                                       n1 = compare2(arr4,n,x2)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr2[1]) & (arr4[5] == arr1[1]):
                                                       n1 = compare2(arr4,x2,n)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr2[1]) & (arr4[5] == arr2[1]):
                                                       n1 = compare2(arr4,x2,x2)
                                                       print(print_num(n1))

                                 elif arr3[0] == arr2[1]:
                                            n = get_lastnum(x2,arr3)
                                            if (arr4[1] == arr1[1]) & (arr4[5] == arr1[1]):
                                                       n1 = compare2(arr4,x1,x1)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr1[1]) & (arr4[5] == arr2[1]):
                                                       n1 = compare2(arr4,x1,n)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr2[1]) & (arr4[5] == arr1[1]):
                                                       n1 = compare2(arr4,n,x1)
                                                       print(print_num(n1))
                                            elif (arr4[1] == arr2[1]) & (arr4[5] == arr2[1]):
                                                       n1 = compare2(arr4,n,n)
                                                       print(print_num(n1))
           except IOError:
                      pirnt("请重新输入")
           else:
                      print("结束")
                                                                                                                                                                 
if __name__=='__main__':
            main()
