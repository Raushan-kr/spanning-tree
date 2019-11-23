def distance(n,dis):
    b=[]
    m=0
    for i in range(n):
        b_temp=['B'+str(i+1),m,'B'+str(i+1)]
        b.append(b_temp)
    for i in range(0,n):
        print('B'+str(i+1),"advertises",b[i])
        
    
    for i in range(n):
        #x=999
        b_temp='B'+str(i+1)
        for j in dis[i]:
                
                b_temp2='B'+str(j+1)
                print(b_temp,' receives',b[j])
                if(b_temp>b[j][0]):
                    #if 
                    b[i]=[b[j][0],b[j][1]+1,'B'+str(i+1)]
                    print('B'+str(i+1),"advertises",b[i])
                    b_temp=b[i][0]
    return(b)
                
                
            
            
           
    
    
    
def routr_config(n,conn,bri,lan):
    print("connections are")
    print(conn)
    print("bridges are:")
    print(bri)
    print("lans are:")
    print(lan)
    
    
    rout=[]
    for j in range (0,n):
        x=conn[j]
        l=x.split()
        b=l[0]
        l.remove(l[0])
        rout.append(l)
        
        print(b,x,l)
    print('rout',rout)
    #return rout
    dis=[]
    for i in range(0,n):
        dis.append(0)
   
    
    for i in range(0,n):
        x=[]
        for j in range(0,n):
            temp2=set()
            temp1=set()
            if i !=j:
                print('i', i , 'j ', j) 
                b=rout[i]
                print(b)
                temp1.update(b)
                b=rout[j]
                print(b)
                temp2.update(b)
                inter=temp1.intersection(temp2)
                print(inter)
                
                if (temp1.intersection(temp2)):
                    
                    x.append(j)
                    
                    print(temp1,temp2)
            dis[i]=x
        print(dis)
    return(distance(n,dis))
        
                    
                    
                    
                    
                    
                    
                    


def radia(n,conn,bri,lan,dis):
    dic={}
    for i in lan:
        dic[i]=' '
        #dist[i]=0
        
    for j in range(0,n):
           
        x=conn[j]
        l=x.split()
        b=l[0]
        print(b)
        l.remove(l[0])
        
        
        for i in l:
            
            
            for j in range(n):
                if b== dis[j][2]:
                    e=dic.get(i)
                    
                    if e==' ' or e[0] >dis[j][0] :
                        dic[i]=dis[j]
                    elif(e[0] ==dis[j][0]and e[1]>dis[j][1]):
                        dic[i]=dis[j]
                    elif(e[0] ==dis[j][0]and e[1]==dis[j][1] and e[2]>dis[j][2]):
                        dic[i]=dis[j]
                   # elif dic.get(i)==dis[j][0] 
                    #print('b',b)
    print(" final lan connection to bridged")            
    print(dic)
    














n=int(input("enter the number of bridges "))
bri=[]
conn=[]
lan=set()
for i in range (0,n):
    print(i)
    
    a=input("enter the connected lan to bride like x1 : 1 2 3 ")
    b1=a.split()
    
    lan.update(b1)
    lan.remove(b1[0])
    conn.append(a)
    bri.append(b1[0])
l=routr_config(n,conn,bri,lan)
print(l)
#distance(n,l)
radia(n,conn,bri,lan,l)
