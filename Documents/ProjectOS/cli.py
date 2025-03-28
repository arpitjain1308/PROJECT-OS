#PROJECT OS 
#BY-ARPIT JAIN

import sys
import os
import pwd
import getpass
import argparse
import builtins

from i18n import _

sudo_user = os.environ.get("SUDO_USER")
doas_user = os.environ.get("DOAS_USER")
pkexec_uid = os.environ.get("PKEXEC_UID")
pkexec_user = pwd.getpwuid(int(pkexec_uid))[0] if pkexec_uid else ""
env_user = getpass.getuser()
user = next((u for u in [sudo_user, doas_user, pkexec_user, env_user] if u), "")

if user == "":
    print(_("Could not determine user, please use the --user flag"))
    sys.exit(1)

parser = argparse.ArgumentParser(
	description=_("Command line interface for Howdy face authentication."),
	formatter_class=argparse.RawDescriptionHelpFormatter,
	add_help=False,
	prog="howdy",
	usage="howdy [-U USER] [--plain] [-h] [-y] {command} [{arguments}...]".format(command=_("command"), arguments=_("arguments")),
	epilog=_("For support please visit\nhttps://github.com/boltgolt/howdy"))

parser.add_argument(
	"command",
	help=_("The command option to execute, can be one of the following: add, clear, config, disable, list, remove, snapshot, set, test or version."),
	metavar="command",
	choices=["add", "clear", "config", "disable", "list", "remove", "set", "snapshot", "test", "version"])

parser.add_argument(
	"arguments",
	help=_("Optional arguments for the add, disable, remove and set commands."),
	nargs="*")

parser.add_argument(
	"-U", "--user",
	default=user,
	help=_("Set the user account to use."))

parser.add_argument(
	"-y",
	help=_("Skip all questions."),
	action="store_true")

parser.add_argument(
	"--plain",
	help=_("Print machine-friendly output."),
	action="store_true")

parser.add_argument(
	"-h", "--help",
	action="help",
	default=argparse.SUPPRESS,
	help=_("Show this help message and exit."))

if len(sys.argv) < 2:
	print(_("current active user: ") + user + "\n")
	parser.print_help()
	sys.exit(0)

args = parser.parse_args()

builtins.howdy_args = args
builtins.howdy_user = args.user

if os.geteuid() != 0:
	print(_("Please run this command as root:\n"))
	print("\tsudo howdy " + " ".join(sys.argv[1:]))
	sys.exit(1)

if args.user == "root":
	print(_("Can't run howdy commands as root, please run this command with the --user flag"))
	sys.exit(1)

if args.command == "add":
	import cli.add
elif args.command == "clear":
	import cli.clear
elif args.command == "config":
	import cli.config
elif args.command == "disable":
	import cli.disable
elif args.command == "list":
	import cli.list
elif args.command == "remove":
	import cli.remove
elif args.command == "set":
	import cli.set
elif args.command == "snapshot":
	import cli.snap
elif args.command == "test":
	import cli.test
else:
	print("Howdy 3.0.0 BETA")
