#
# deoldify ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import subprocess, os, re
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
Gstr_title = r""" 
     _            _     _ _  __       
    | |          | |   | (_)/ _|      
  __| | ___  ___ | | __| |_| |_ _   _ 
 / _` |/ _ \/ _ \| |/ _` | |  _| | | |
| (_| |  __/ (_) | | (_| | | | | |_| |
 \__,_|\___|\___/|_|\__,_|_|_|  \__, |
                                 __/ |
                                |___/ 
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       deoldify

    SYNOPSIS

        docker run --rm fnndsc/pl-deoldify deoldify                     \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-deoldify deoldify                        \
                /incoming /outgoing

    DESCRIPTION

        `deoldify` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Deoldify(ChrisApp):
    """
    An app to convert old images to color images
    """
    PACKAGE                 = __package__
    TITLE                   = 'A Chris Plugin for Deoldify.'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        print('Conversion of old images to color images %s' % (options.inputdit, options.outputdir))
        for filename in os.listdir(options.inputdir):
            inputpath = os.path.join(options.inputdir, filename)
            outputpath = os.path.join(options.outputdir, re.sub('\.\w+', '.jpg',filename ))
            # parser = ArgumentParser("Parse the input arguments for the deoldify script", formatter_class=ArgumentDefaultsHelpFormatter)
        
    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
