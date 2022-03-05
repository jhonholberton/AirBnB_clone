#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """class that inherits from cmd module"""
    prompt = "(hbnb) "
    list_class = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """"EOF command to exit the program"""
        exit()

    def emptyline(self):
        """method to keep line empty"""
        pass

    def do_create(self, arg):
        """"Creates a new instance of BaseModel"""
        if arg == '':
            print("** class name missing **")
        elif arg not in self.list_class:
            print("** class doesn't exist **")
        else:
            my_object = eval(arg + "()")
            my_object.save()
            print(my_object.id)

    def do_show(self, arg):
        """show de object Basemodel for ID"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(arg[0], arg[1])
            if k in storage.all().keys():
                print(storage.all()[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """this method delete basemodel id complete"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(arg[0], arg[1])
            if k in storage.all().keys():
                storage.all().pop(k)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """method to Prints all string representation of all instances"""
        arg = arg.split()
        if arg[0] not in self.list_class:
            print("** class doesn't exist **")
        else:
            new_list = []
            for v in storage.all().values():
                cadena = str(v.__str__())
                new_list.append(cadena)
            print(new_list)

    def do_update(self, arg):
        """method to update a instances"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            k = "{}.{}".format(arg[0], arg[1])
            arg[3] = int(arg[3]) if arg[3][0] != '"' else arg[3][1:-1]
            if k in storage.all().keys():
                v = storage.all()[k]
                v.__dict__[arg[2]] = arg[3]
                storage.all()[k] = v
                storage.save()
            else:
                print("** no instance found **")
        
        
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
