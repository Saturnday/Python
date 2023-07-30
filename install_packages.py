""""
package manager
pippy.com
pip install cowsay
the package installed globaly, the issue was that i had second python installed and a virtual environment for it so it messed up
coz i didn't add the package to the virtual invironent of this project i won't be able to launch this without instlaling the package to the new machine 

"""

import cowsay
import sys
cowsay.stegosaurus('Hello,'+sys.argv[1])






