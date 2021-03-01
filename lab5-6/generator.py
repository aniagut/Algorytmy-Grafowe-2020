import random
import datetime


def random_date(start_date,days_between_dates):
    random_number_of_days=random.randrange(days_between_dates)
    return (start_date+datetime.timedelta(random_number_of_days)).strftime('%m/%d/%Y')
def random_id(min,max):
    return random.randint(min,max)
def random_money(min,max):
    return round(random.uniform(min,max),2)

def random_col(amount,minid,maxid,minmoney,maxmoney,startdate,daysbetween):
    for i in range(1,amount+1):
        print("insert into wplaty (id, naleznosci_id, kwota, data_wplaty) values ("+i.__str__()+","+random_id(minid,maxid).__str__()+","+random_money(minmoney,maxmoney).__str__()+", '"+random_date(startdate,daysbetween).__str__()+"');")

start_date=datetime.date(2018,5,1)
end_date=datetime.date(2020,5,31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days


random_col(2000,1,1000,50,3000,start_date,days_between_dates)