
from copy_func import copy_dir
from gen_site_recur import generate_pages_recursive

def main():
    copy_dir("static", "public")
    
    generate_pages_recursive(
    "/home/risamc/workspace/github.com/Risamc/Static_site_gen/content",
    "/home/risamc/workspace/github.com/Risamc/Static_site_gen/template.html",
    "/home/risamc/workspace/github.com/Risamc/Static_site_gen/public"
    )


main()
