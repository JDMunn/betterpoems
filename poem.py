class Poem:
  def __init__(self, filename):
    with open(filename) as f:
      self.text = f.read()
    self.text_arr = self.text.split()
    self.annotations = []