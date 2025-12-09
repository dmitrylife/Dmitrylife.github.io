import os

def print_tree(startpath, indent="", exclude_dirs=None, exclude_files=None, exclude_ext=None):
    exclude_dirs = {d.lower() for d in (exclude_dirs or [])}
    exclude_files = {f.lower() for f in (exclude_files or [])}
    exclude_ext = {e.lower() for e in (exclude_ext or [])}

    try:
        items = sorted(os.listdir(startpath))
    except PermissionError:
        print(indent + "⚠️ [Доступ запрещён]")
        return

    for i, item in enumerate(items):
        path = os.path.join(startpath, item)
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "

        name_lower = item.lower()
        ext_lower = os.path.splitext(item)[1].lower()

        # Исключаем ненужные директории, файлы и расширения
        if os.path.isdir(path) and name_lower in exclude_dirs:
            continue
        if os.path.isfile(path) and (name_lower in exclude_files or ext_lower in exclude_ext):
            continue

        print(indent + prefix + item)

        if os.path.isdir(path):
            new_indent = indent + ("    " if is_last else "│   ")
            print_tree(path, new_indent, exclude_dirs, exclude_files, exclude_ext)


if __name__ == "__main__":
    project_path = "."  # Укажи свой путь

    exclude_dirs = [
        "__pycache__", ".git", ".venv", ".idea", "migrations",
        "staticfiles", "static", "media", "logs", "middlewares"
    ]
    exclude_files = [
        "manage.py", "deploy_server.sh", "requirements.txt",
        "__init__.py", ".gitignore", ".env"
    ]
    exclude_ext = [".pyc", ".sh"]

    print_tree(project_path, exclude_dirs=exclude_dirs, exclude_files=exclude_files, exclude_ext=exclude_ext)
