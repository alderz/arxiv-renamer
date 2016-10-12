import feedparser

class Article:
    """ Class for interfacing with the arxiv article metadata. """

    def __init__(self, article_id):
        self.article_id = article_id
        self.url = 'http://export.arxiv.org/api/query?id_list={}'.format(self.article_id)
        self.fetch()

    def fetch(self):
        data = feedparser.parse(self.url)
        entry = data['entries'][0]
        self.authors = [x['name'] for x in entry['authors']]
        self.title = entry['title'].replace('\n', '')

        # Take only last word from author strings.
        self.authors = [x.split()[-1] for x in self.authors]

        # published_parsed is added by feedparser.
        self.year = entry['published_parsed'].tm_year


    def authors_string(self):
        if (len(self.authors) == 1):
            return self.authors[0]
        elif (len(self.authors) == 2):
            return "{} and {}".format(self.authors[0], self.authors[1])
        else:
            return "{} et al.".format(self.authors[0])

    def year_string(self):
        return str(self.year)

    def filename_string(self):
        return "[{} {}] {}".format(self.authors_string(), self.year_string(),
                self.title)
