from typing import List

#import List for type hinting
def get_cats_info(path: str) -> List[object]:
    cats_info = []
    try:
        with open(path, "r", encoding="UTF-8") as file_data:
            ids = []
            for line in file_data:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    #we assume that data is correct if we got 3 chunks
                    if cat_data[0] in ids:
                        #error, uniquie id duplicated
                        print(f"Duplicate ID in line: '{line}'")
                        continue

                    cat = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat)
                    ids.append(cat_data[0])
                    #save id for next iterations   
                else:
                    print(f"Incorrect data format '{line}'")    
  
    except FileNotFoundError:
        print(f"File '{path}' not found!")

    except Exception as ex:
        print(f"An error occurred: {ex}")
    
    finally:
        return cats_info

cats_info = get_cats_info("data/cats.txt")
print(cats_info)
