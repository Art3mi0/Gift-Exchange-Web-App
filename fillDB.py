from app import db, User

def popDB(db):
    test = User(name='test', password='test')
    temo = User(name='Temo123', password='temo')
    brandon = User(name='Brandon', password='Brandon')
    ligma = User(name='LIGMA', password='test')

    db.session.add(test)
    db.session.add(temo)
    db.session.add(brandon)
    db.session.add(ligma)
    db.session.commit()
