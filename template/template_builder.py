class TemplateBuilder:
  def init_readme(self, name = "Sample"):
    text_file = open('./template/files/init-readme.txt', 'r')
    init_readme_text = text_file.read()
    text = """
      # %s Project
      """ % (name)
    return text.lstrip() + init_readme_text
  def init_resource_readme(self, name = "Sample"):
    text_file = open('./template/files/init-resources.txt', 'r')
    init_resources_text = text_file.read()
    text = """
      # %s Project
      """ % (name)
    return text.lstrip() + init_resources_text
  def init_courses_readme(self, name = "Sample"):
    text_file = open('./template/files/init-courses.txt', 'r')
    init_courses_text = text_file.read()
    text = """
      # %s Project
      """ % (name)
    return text.lstrip() + init_courses_text
  def init_praxi(self, git_name, name, description):
    text_file = open('./template/files/praxi.txt', 'r')
    praxi_text = text_file.read()
    dynamic_praxi_text = praxi_text % (git_name, name, description)
    return dynamic_praxi_text.lstrip()