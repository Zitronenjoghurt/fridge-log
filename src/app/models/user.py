import reflex as rx

class User(rx.Model, table=True):
    username: str