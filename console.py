#!/usr/bin/python3
"""console foy my API"""
import cmd
from xxlimited import new
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
    list_class = ["BaseModel", "User", "State",
                  "City", "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """"EOF command to exit the program"""
        exit()

    def emptyline(self):
        """method to keep line empty"""
        pass

    def default(self, arg):
        """control default line comand"""
        arg = arg.split(".")
        new_arg = arg[1].split("(")
        if new_arg[0] == 'all':
            self.do_all(arg[0])
        elif new_arg[0] == 'count':
            self.do_count(arg[0])
        elif new_arg[0] == 'show':
            new_show = new_arg[1].split("\"")
            send_line = arg[0] + " " + new_show[1]
            self.do_show(send_line)
        elif new_arg[0] == 'destroy':
            new_show = new_arg[1].split("\"")
            send_line = arg[0] + " " + new_show[1]
            self.do_destroy(send_line)
        elif new_arg[0] == 'update':
            is_dict = new_arg[1].find("}")
            if is_dict == -1:
                self.do_newstring(new_arg[1], arg[0])
            else:
                delete = ",)\"'}:"
                new_list = new_arg[1].split("{")
                for x in range(len(delete)):
                    new_list[0] = new_list[0].replace(delete[x], "")
                for x in range(len(delete)):
                    new_list[1] = new_list[1].replace(delete[x], "")
                lis_dict = new_list[1].split(" ")
                for i in range(0, len(lis_dict), 2):
                    try:
                        int(lis_dict[i + 1])
                    except Exception:
                        lis_dict[i + 1] = '"' + lis_dict[i + 1] + '"'
                    send_line = arg[0] + " " + new_list[0] + \
                        lis_dict[i] + " " + lis_dict[i + 1]
                    self.do_update(send_line)
        else:
            pass

    def do_newstring(self, arg, my_class):
        delete = ",)\""
        for x in range(len(delete)):
            arg = arg.replace(delete[x], "")
        new_update = arg.split(" ")
        try:
            int(new_update[2])
        except Exception:
            new_update[2] = '"' + new_update[2] + '"'
        send_line = my_class + " " + new_update[0] + \
            " " + new_update[1] + " " + new_update[2]
        self.do_update(send_line)

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

    def do_count(self, arg):
        """show de object Basemodel for ID"""
        arg = arg.split()
        count = 0
        for v in storage.all().values():
            if arg[0] == type(v).__name__:
                count += 1
        print(count)

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
        if len(arg) == 0:
            new_list = []
            for v in storage.all().values():
                cadena = str(v.__str__())
                new_list.append(cadena)
            print(new_list)
        elif arg[0] not in self.list_class:
            print("** class doesn't exist **")
        else:
            new_list = []
            for v in storage.all().values():
                if arg[0] == type(v).__name__:
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
    """main name principal"""
    HBNBCommand().cmdloop()
