from app import db, Puppy

# create
my_puppy = Puppy('Joe', 52)
db.session.add(my_puppy)
db.session.commit()

# read

all_puppies = Puppy.query.all()
print(all_puppies)

# select by id

puppy1 = Puppy.query.get(1)
print(puppy1)

# filters
# produces sqlcode
puppy_frankie = Puppy.query.filter_by(name='Frank')

print(puppy_frankie.all())

# update
print(puppy1)
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
print(first_puppy)

# delete

second_puppy = Puppy.query.get(3)
db.session.delete(second_puppy)
db.session.commit()

# all
puppy1 = Puppy.query.all()
print(puppy1)
