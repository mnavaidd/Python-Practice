def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', '27')
artists = build_person('nasir', 'asad')
print(musician)
print(artists)


##
def make_album(artist_name, artist_title, number_of_track=''):
    album = {'name': artist_name, 'title': artist_title}
    return album
album1 = make_album('Navaid', 'Best song')
for k,v in album1.items():
    print(k,v)


##
def greet_users(x):
    y=x*2
    print(y)
    return y
x=10
z= greet_users(x)
print(x)
print(z)
