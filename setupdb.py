from app import db,Puppy  
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frank', 5)

print (sam.id)

db.session.add_all([sam,frank])
db.session.commit()


print(sam.id)
print(frank.id)