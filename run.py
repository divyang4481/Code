from lms import app, db
from lms.models import User  # 

def initialize_database():
    db.create_all()

    # Conditional seeding
    if User.query.count() == 0:
        admin_user = User(username='admin', is_admin=True)
        admin_user.set_password('admin123')  # Assuming you have a method to hash passwords
        db.session.add(admin_user)
        
        # Add more initial data as needed
        
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
    with app.app_context():
        initialize_database()
    #app.run(debug=True)
    app.run(debug=True)
