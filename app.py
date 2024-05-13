from flask import Flask, render_template

app = Flask(__name__)

projects = [
   {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-mvu2.onrender.com/"
   },
   {
         "name": "Online Library app with Javascript and css",
        "thumb": "img/e-book.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["Javascript", "web"],
        "slug": "online-library",
        "prod": "https://ebook-library0.netlify.app/"
   },
   {
        "name": "Online Food app with Javascript and css",
        "thumb": "img/food-app.jpg",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["Javascript", "web"],
        "slug": "online-food",
        "prod": "https://omnifoodkunal.netlify.app/"
   },
   {
       "name": "Travel app with Javascript and css",
        "thumb": "img/the-road.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["Javascript", "web"],
        "slug": "travel-app",
        "prod": "https://travelkunal.netlify.app/"
   },
   {
       "name": "wine buying app with Javascript and css",
        "thumb": "img/wine-shot.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["Javascript", "web"],
        "slug": "wine-app",
        "prod": "https://winekunal.netlify.app/"
   }
   
]

slug_to_project = {project["slug"]:project for project in projects}
@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


