class Poem:
  def __init__(self, filename):
    with open(filename) as f:
      self.text = f.read()
    self.text_arr = self.text.split()
    self.annotations = []

  def add_annotation(self, start, end, content, print_output = True):
    self.annotations.append(Annotation(start, end, content))
    if print_output:
      print "Added annotation!"

  def view_annotations(self):
    for a in self.annotations:
      print 'text:', " ".join(self.text_arr[a.start:a.end])
      print 'annotation:', a.content
      print

class Annotation:
  def __init__(self, start, end, content):
    # Takes a poem object as argument
    self.start = start
    self.end = end
    self.content = content