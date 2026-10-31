#returns list of dict with cats' info
def get_cats_info(path):
    try:
        with open(path, mode="r", encoding="utf-8") as f:
            cats_info = list()
            current_line = 0

            for line in f:
               
                current_line += 1
                line = line.strip()

                if not line:
                    continue
                
                try:
                    cat_id, cat_name, cat_age = (part.strip() for part in line.split(","))

                except ValueError:
                    print(f"line {current_line} is corrupted. will not be displayed")
                    continue

                # supposing business rules only allow alphanumeric cat id, with fixed length of 24 characters
                # name that has only letters
                # age has to be digits only
                # the order of attributes is fixed
                error_message = ""

                if not cat_id.isalnum() or len(cat_id) != 24:
                    error_message = f"line {current_line} has invalid cat_id"
                if not cat_name.isalpha():
                    error_message += f"line {current_line} has invalid cat's name" if not error_message else " and invalid cat's name"
                if not cat_age.isdigit():
                    error_message += f"line {current_line} has invalid cat's age" if not error_message else " and invalid cat's age"

                if error_message:
                    print(error_message)
                    continue

                #only create a dict if cat info is valid 
                cat_item = dict()

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