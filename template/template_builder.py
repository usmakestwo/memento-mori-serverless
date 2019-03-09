class TemplateBuilder:
  def __init__(self):
    print("Initialize Template Builder")
  def init_readme(self, name = "Sample"):
    text = """
      # %s Repo

      Lets see if this works, it it does, that is very cool!

      This is a code:

      `var a = {}`

      And this is a *Bold*.

      """ % (name)
    return text
  def init_resource_readme(self, name = "Sample"):
    text = """
      # %s Repo

      Lets see if this works, it it does, that is very cool!

      This is a code:

      `var a = {}`

      And this is a *Bold*.

      """ % (name)
    return text
  def init_courses_readme(self, name = "Sample"):
    text = """
      # %s Repo

      Lets see if this works, it it does, that is very cool!

      This is a code:

      `var a = {}`

      And this is a *Bold*.

      """ % (name)
    return text