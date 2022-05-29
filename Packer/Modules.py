import json
import os
modules_path = os.path.join(os.path.abspath(".."), "modules")


class Module:
    id: str
    name: dict
    description: dict
    version: str
    weight: int
    incompatible: list
    author: str
    files: list[str]

    def __init__(self,
                 id: str,
                 author: str,
                 name: dict,
                 description: dict,
                 version: str,
                 weight: int,
                 incompatible: list):
        self.id = id
        self.author = author
        self.name = name
        self.description = description
        self.version = version
        self.weight = weight
        self.incompatible = incompatible
        module_path = os.path.join(modules_path, id, "assets")
        self.files = os.listdir(module_path)
        for i in self.files:
            self.files.remove(i)
            i = os.path.join(module_path, i)
            self.files.append(i)
            if os.path.isdir(i):
                self.files.remove(i)
                self.files.extend(os.listdir(i))


def load_modules() -> list[Module]:
    modules_list = os.listdir(modules_path)
    modules: list = []
    for module_name in modules_list:
        module_path = os.path.join(modules_path, module_name)
        module_meta = os.path.join(module_path, "module.mcmeta")
        with open(module_meta, "r", encoding="utf8") as f:
            module_meta = json.loads(f.read())
            f.close()
        modules.append(Module(module_meta["id"], module_meta["author"], module_meta["name"], module_meta["description"],
                              module_meta["version"], module_meta["weight"], module_meta["incompatible"]))
    return modules


print(load_modules()[0].files)
