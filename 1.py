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
                      
def get_type(ty_pe,x):
            if ty_pe == '整数':
                        x = int(x)
            elif ty_pe == '浮点数':
                        x = float(x)
            return x
                        
def get_lastnum(n,sym,num):   
            if sym == '增加':
                        n = n+num
            elif sym == '减少':
                        n = n-num
            return n
            
def get_change(n):
            for key in dic_num:
                        if n == dic_num[key]:
                                    return key

def judge(n,jd_sym,jd_num,word1,word2):
            word1=word1.strip('“”')  #去除双引号
            word2=word2.strip('“”')
            if  jd_sym == '大于':
                        if n > jd_num:
                                    print(word1)
                        else:
                                    print(word2)
            
def main():
            s1 = input()
            s2 = input()
            s3 = input()
            s4 = input()
            s5 = input()
            
            ty_pe=s1.split(' ')[0]#获取变量类型             
            num=s1.split(' ')[3] #提取原始数据值
            t =  dic_num[num]  #通过字典实现数字转化
            t = get_type(ty_pe,t)  #类型转化

            sym2=s2.split(' ')[1] #拆分提取运算符号           
            num2=s2.split(' ')[2] #拆分提取运算数字
            t2 = dic_num[num2]  #数字转化  
            t = get_lastnum(t,sym2,t2) #进行运算

            sym3=s3.split(' ')[1]#拆分提取运算符号         
            num3=s3.split(' ')[2]  #拆分提取运算数字
            t3 = dic_num[num3]  #数字转化 
            t = get_lastnum(t,sym3,t3) #进行运算

            jd_sym = s5.split(' ')[2] #提取判断符号
            
            jd_num=s5.split(' ')[3]  #提取判断数字
            jd_num = dic_num[jd_num]  #数字转化
            
            word1=s5.split(' ')[6] #获得句子1
            word2=s5.split(' ')[9] #获得句子2

            print(get_change(t))  #将阿拉伯数字转化为汉字
            judge(t,jd_sym,jd_num,word1,word2) #判断
              
if __name__=='__main__':
            main()
  
