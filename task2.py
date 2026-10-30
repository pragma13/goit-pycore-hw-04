#returns list of dict with cats' info
def get_cats_info(path):
    try:
        with open(path, mode="r", encoding="utf-8") as f:
            cats_info = list()
            current_line = 0

            for line in f:
                cat_item = dict()
                current_line += 1
                line = line.strip()

                if not line:
                    continue
                
                try:
                    cat_id, cat_name, cat_age = line.split(",")
                except ValueError:
                    print(f"line {current_line} is corrupted. will not be displayed")
                    continue

                cat_item["id"] = cat_id
                cat_item["name"] = cat_name
                cat_item["age"] = cat_age
                cats_info.append(cat_item)

            return cats_info

    except FileNotFoundError:
        print(f"file {path} is not found")
        return []
    except PermissionError:
        print(f"no permission to read the file {path}")
        return []
    except UnicodeDecodeError:
        print("file couldn't be read in utf8")
        return []
    except IsADirectoryError:
        print(f"{path} is a directory")
        return []


print(get_cats_info("cats.txt"))