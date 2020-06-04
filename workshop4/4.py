from conect import engine
from sqlalchemy.orm import sessionmaker
from mod import users, taxi, zamov
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

bob = users(user_id = 1, user_name='Bob', user_phone ='+38099999444')
boba  = users(user_id = 2, user_name='Boba', user_phone = '+38055565555')

session.add(bob)
session.commit()
session.add(boba)
session.commit()

bob_id = (session.query(users).filter(users.user_phone == '+380999994449')[0]).user_id
boba_id = (session.query(users).filter(users.user_phone == '+380555655550')[0]).user_id

car1 = taxi(taxi_id=15555, name_company = "Uber", car="Ua0999", price = 5)
car2 = taxi(taxi_id=155225, name_company = "Uclone", car="Ua98-37k", price = 7)

bobs_zamov = zamov(id_user = bob_id, id_taxi=15555, date_c = func.current_date(), place_A ='Qeewrww-1', place_B ='Qwrww-154')
bobas_zamov = zamov(id_user = boba_id, id_taxi=155225, date_c = func.current_date(), place_A ='Dec 1a', place_B ='wol 14')


'''instances = [bobs_zamov, bobas_zamov,car1,car2]
session.add_all(instances)
# for ins in instances:
#     session.add(ins)
#     session.commit()'''