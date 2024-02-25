#PART 1:

import os
import shutil

#Creating Directory Tree

def create_directory_tree():
    try:
        os.makedirs("draft_code/pending")
        os.makedirs("draft_code/complete")
        os.makedirs("includes")
        os.makedirs("layout/default")
        os.makedirs("layout/post/posted")
        os.makedirs("site")

        print("Directory tree created sucesssfully")
    except Exception as e:
        print(f"Error: {e}")

# Deleting Direct. Tree

def delete_directory_tree():
    try:
        shutil.rmtree("draft_code")
        shutil.rmtree("includes")
        shutil.rmtree("layout")
        shutil.rmtree("site")
        print("Directory tree deleted sucessfully")
    except Exception as e:
        print(f"Error: {e}")


create_directory_tree()
delete_directory_tree()