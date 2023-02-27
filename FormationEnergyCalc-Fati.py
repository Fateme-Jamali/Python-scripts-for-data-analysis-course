import pandas as pd
import re
import numpy as np
import pandas as pd
df_AX = pd.read_csv("AX-finalenthlpy.csv")
df_AX.set_index('final-enthalpy(Ry)', inplace=True)
df_BX = pd.read_csv("BX2-finalenthlpy.csv")
df_BX.set_index('final-enthalpy(Ry)', inplace=True)
df_BX['BX2'] = df_BX['BX2'].apply(lambda r: '_'.join(r.split('_')[:-1]))
#display(df_AX)
#display(df_BX)
df = pd.DataFrame(columns=['StructureName','Formation-energy(eV)'])
df2 = pd.read_csv('FE-from53random.csv')
df['StructureName']=df2['StructureName']
#df
FE=[]
with open('Inputfile.csv') as fp:
    next(fp)
    for line in fp:
        num_A1A2BX=float(line.split(",")[1])
        line1=line.split(",")[0]
        A1,A2,BX3=line1.split("_")
        #print(line1,A1,A2,BX3)
        BX=BX3[:-1]
        B=re.findall('[A-Z][^A-Z]*', BX)[0]
        X=re.findall('[A-Z][^A-Z]*', BX)[1]
        #print(B,X)
        A1A2BX=A1+A2+B+X
        A1X=A1+X
        num_A1X=df_AX.index[df_AX['AX'] == A1X].tolist()
        A2X=A2+X
        num_A2X=df_AX.index[df_AX['AX'] == A2X].tolist()
        #print(A1X, *num_A1X , A2X, *num_A2X)
        BX=B+X+"2"
        num_BX=df_BX.index[df_BX['BX2'] == BX].tolist()
        #print(BX,*num_BX)
        #print(line1, num_A1A2BX)
        num_A1X=np.array(num_A1X,dtype=float)
        num_A1X = np.float64(num_A1X)
        num_A2X=np.array(num_A2X,dtype=float)
        num_A2X = np.float64(num_A2X)
        num_BX=np.array(num_BX,dtype=float)
        num_BX = np.float64(num_BX)
        res1=(num_A1A2BX)
        res2=(num_A1X)+(num_A2X)+(2*(num_BX))
        res3=(res1-res2)*13.6056980659
        #print(type(res3) , res3)
        #print(A1A2BX,A1X,A2X,BX,num_A1A2BX,num_A1X,num_A2X,num_BX, res3)
        #print(A1A2BX, A1X,A2X,BX,type(num_A1A2BX), type(num_A1X),type(num_A2X),type(num_BX))
        #print(type(res3))
        #res3=res3.tolist()
        #print(type(res3))
        FE.append(res3)
#print( type(FE))
df['Formation-energy(eV)']=FE
#df = pd.DataFrame(FE, columns=['Formation-energy(eV)'])
df.to_csv('outputfile.csv')