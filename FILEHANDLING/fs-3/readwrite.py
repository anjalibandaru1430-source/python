fp1=open('data.txt','r')
fp2=open('data.txt','w')
data=fp1.read()
fp2.write(data)

fp1.close()
fp2.close()