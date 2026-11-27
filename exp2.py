
def bold(func):
    def wrapper(text):
        return "**" + func(text) + "**"
    return wrapper


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def create_report(cls, title, content):
        return cls(title, content)

    @bold
    def format_text(self):
        return self.content

    def __str__(self):
        return self.title + "\n" + self.format_text()


# Main program
r = Report.create_report("Python Report", "Welcome to Advanced Python")

print(r)
