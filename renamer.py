import sys
import os
import arxiv

def main():
    if len(sys.argv) <= 1:
        print("Usage: renamer.py file1 [file2 file3...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        print("Processing {}.".format(path))
        if not os.path.isfile(path):
            print("{} is not a file.".format(path))
        filename = os.path.basename(path)
        filedir = os.path.dirname(path)
        extension = os.path.splitext(filename)[1]

        article_id = os.path.splitext(filename)[0]
        article = arxiv.Article(article_id)

        new_filename = "{}{}".format(article.filename_string(), extension)
        new_path = os.path.join(filedir, new_filename)
        print("Renaming {} to {}.".format(path, new_path))
        os.rename(path, new_path)

if __name__ == "__main__":
    main()
