class Poem:
  def __init__(self, filename):
    with open(filename) as f:
      self.text = f.read()
    self.words = self.text.split()
    self.lines = self.text.split("\n")
    self.annotations = []

  def annotate_word(self, start, end, content, print_output = True):
    self.annotations.append(Annotation(start, end, content))
    if print_output:
      print "Added annotation!"

  def annotate_line(self, start, end, content, print_output = True):


  def view_annotations(self):
    for a in self.annotations:
      print 'text:', " ".join(self.words[a.start:a.end])
      print 'annotation:', a.content
      print

class Annotation:
  def __init__(self, start, end, content, type):
    # Takes a poem object as argument
    self.start = start
    self.end = end
    self.content = content
    self.type = type # 'line' or 'word'