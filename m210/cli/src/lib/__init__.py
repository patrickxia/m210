# Standard modules.
import os.path
import sys

# Third-party modules.
import dbus.exceptions

# Project modules.
import m210.daemon

def error_and_exit(msg):
    prog = os.path.basename(sys.argv[0])
    print >>sys.stderr, "%s: error: %s" % (prog, msg)
    sys.exit(1)

def get_interface_or_exit():
    try:
        return m210.daemon.Interface()
    except dbus.exceptions.DBusException, e:
        if e.get_dbus_name() == "org.freedesktop.DBus.Error.ServiceUnknown":
            error_and_exit("%s is not available" % m210.daemon.NAME)
        raise e
