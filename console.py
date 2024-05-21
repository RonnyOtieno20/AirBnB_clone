#!/usr/bin/python3
"""ALX command prompt to manage models"""
import cmd
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on CTRL+D"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print string representations of all instances"""
        args = shlex.split(arg)
        objects = storage.all()
        instances = []
        if not args:
            for obj in objects.values():
                instances.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            for obj_id, obj in objects.items():
                if obj_id.startswith(class_name):
                    instances.append(str(obj))
        print(json.dumps(instances))

    def do_update(self, arg):
        """Update an instance by adding or updating attribute"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        instance = objects[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_update2(self, arg):
        """Update an instance by adding or updating attributes from a dict"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        instance = objects[key]
        attr_dict = json.loads("{" + arg.split("{")[1])
        for attr_name, attr_value in attr_dict.items():
            setattr(instance, attr_name, attr_value)
        instance.save()

    def do_count(self, arg):
        """Count instances of a class"""
        class_name = shlex.split(arg)[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        objects = storage.all()
        for obj_id in objects:
            if obj_id.startswith(class_name):
                count += 1
        print(count)

    def default(self, line):
        """Handle alternative command syntax"""
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        args = line.split(".")
        if len(args) < 2:
            super().default(line)
            return
        class_name = args[0]
        method_name = args[1].split("(")[0]
        if method_name not in methods:
            super().default(line)
            return
        method = methods[method_name]
        arg_str = args[1].split("(")[1][:-1]
        if arg_str:
            args = shlex.split(arg_str)
            args.insert(0, class_name)
            method(" ".join(args))
        else:
            method(class_name)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
