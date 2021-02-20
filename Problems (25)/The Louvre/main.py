class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


picture = Painting(
    str(input()),
    str(input()),
    str(input())
)

print('"' + picture.title + '"',
      'by',
      picture.painter,
      '(' + picture.year + ')',
      'hangs in the',
      picture.museum + '.')
