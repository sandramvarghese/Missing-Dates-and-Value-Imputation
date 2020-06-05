import datetime
import pandas as pd
def imputevalue(D):
    dl=[]
    for x in D:
        d = datetime.datetime.strptime(x, '%Y-%m-%d')
        dl.append(d)
    dl = sorted(dl)
    all_dates =list(pd.date_range(dl[0].date(),dl[-1].date()))
    missing_dates = list(set(all_dates) - set(dl))
    for i in missing_dates:
        previousd=i.date()-datetime.timedelta(days=1)
        nextd = i.date()+datetime.timedelta(days=1)
        midDate=i
        dl.append(midDate)
        D[str(midDate.date())]=int(((float((D[str(previousd)]))+float(D[str(nextd)]))/2))
    dl=sorted(dl)
    D1={}
    for i in dl:
        D1[str(i.date())]=D[str(i.date())]
    return(D1)
D= {"2019-01-05":"105","2019-01-03":"115" , "2019-01-01":"95"}
print("before imputation \n" , D)
D=imputevalue(D)
print("after imputation \n",D )


###           Output

###           before imputation 
###           {'2019-01-05': '105', '2019-01-03': '115', '2019-01-01': '95'}
###           after imputation 
###           {'2019-01-01': '95', '2019-01-02': 105, '2019-01-03': '115', '2019-01-04': 110, '2019-01-05': '105'}