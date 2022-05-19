from app import app
from flask import render_template
from models.order_list import orders


@app.route("/")
def index():
    return "Might Meal Menu"


@app.route("/Orders")
def get_orders():
    return render_template("index.html", title="Orders Page", orders=orders)


@app.route("/Orders/<index>")
def see_order(index):
    return render_template(
        "order.html", title="customer order", order=orders[int(index)]
    )
