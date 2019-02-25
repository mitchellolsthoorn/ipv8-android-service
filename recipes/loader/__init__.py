from __future__ import absolute_import
from os import getenv
from os.path import join, exists
from sh import mkdir, cp
from pythonforandroid.toolchain import PythonRecipe, current_directory


class LocalLoaderRecipe(PythonRecipe):
    """
    Python-for-Android IPV8 loader recipe
    """

    url = 'git+https://github.com/mitchellolsthoorn/ipv8-dapps-loader.git'

    depends = ['openssl', 'libtorrent', 'ipv8']

    patches = []

    python_depends = []

    site_packages_name = 'loader'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(LocalLoaderRecipe, self).postbuild_arch(arch)

        # Install twistd plugins
        cp('-rf', join(self.get_build_dir(arch.arch), 'twisted'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))

        # Install web interface
        cp('-rf', join(self.get_build_dir(arch.arch), 'web'), self.ctx.get_python_install_dir())
        cp('-rf', join(self.get_build_dir(arch.arch), 'web'), join(self.ctx.get_python_install_dir(), 'lib'))
        cp('-rf', join(self.get_build_dir(arch.arch), 'web'), './')


recipe = LocalLoaderRecipe()
