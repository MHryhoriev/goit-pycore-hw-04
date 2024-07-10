from processing_cats import get_cats_info

def main():
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)

if __name__ == "__main__":
    main()