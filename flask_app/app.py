from flask import Flask, request, render_template_string

app = Flask(_name_)

# Homepage route
def home():
    return "Hello, World!"

# Form route
def greet():
    form_html = """
    <form method="post">
        Name: <input type="text" name="name" required><br>
        Age: <input type="number" name="age" required><br>
        <input type="submit" value="Greet">
    </form>
    """
    
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if not name or not age.isdigit():
            return "Invalid input. Please enter a valid name and age." + form_html
        return f"Hello, {name}! You are {age} years old."
    
    return form_html

app.add_url_rule("/", "home", home)
app.add_url_rule("/greet", "greet", greet, methods=["GET", "POST"])

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)