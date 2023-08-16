from fastapi import FastAPI, Response
from jinja2 import Environment, PackageLoader

app = FastAPI()

# Set Jinja2 template engine
env = Environment(loader=PackageLoader('main', 'templates'))


# Define Root endpoint
@app.get("/")
def index():
  # Render index.html
  template = env.get_template('index.html')
  context = {
    'title': 'FastAPI',
  }
  return Response(template.render(context))


if __name__ == '__main__':
  app.run(debug=True)
