# Configure openalea environment variables


from install_lib import get_default_dyn_lib
# from util import check_system
from command import set_env
import os, sys
from optparse import OptionParser
    
def main():

    # options
    parser = OptionParser()
    parser.add_option( "--install-dyn-lib", dest="lib_dir",
                       help="Set the dynamic library path",
                       default=None)

    (options, args)= parser.parse_args()

    set_env(options.lib_dir)

#     env = check_system()

#     if('posix' in os.name):
#         for k, v in env.items():
#             print "export %s=%s\n"%(k, v)
            
#     elif('win' in sys.platform):
#         for k, v in env.items():
#             print "set %s=%s\n"%(k, v)





if(__name__ == '__main__'):
    main()