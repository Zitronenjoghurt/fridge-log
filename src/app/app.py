import reflex as rx

from .models.user import User


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    test = User(username="test")
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!"),
            rx.hstack(
                rx.button("Decrease", on_click=State.decrement),
                rx.heading(State.count),
                rx.button("Increase", on_click=State.increment),
            ),
        ),
        padding="100px",
    )

app = rx.App()
app.add_page(index)