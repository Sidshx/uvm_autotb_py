import os
def file_check(uvm_files, files):

    for name in files:
        path = os.path.join(uvm_files, name)
        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted: {path}")
    print("Ready for generating files!")
         
   
