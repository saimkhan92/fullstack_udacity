
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template("menu.html", restaurant=restaurant, items=items)

@app.route("/restaurant/<int:restaurant_id>/new/")
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/")
def editMenuItem(restaurant_id, menu_id):
    editedItem=session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method=="POST":
        if request.form["name"]:
            editedItem.name= request.form["name"]
        session.add(editedItem)
        session.commit()
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template("newmenuitem.html", restaurant_id=restaurant_id)

@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/")
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

























