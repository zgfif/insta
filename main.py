from applib.extract_and_save import ExtractAndSave


def main():
    urls = ['https://instagram.com/pashabratanov',]
    ExtractAndSave(urls=urls).perform()



if __name__ == '__main__':
    main()
