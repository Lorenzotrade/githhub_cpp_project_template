from conans import ConanFile

class OlfConan(ConanFile):
    license = "<Todo>"
    url = "<Todo>"
    description = "<Todo>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    revision_mode = "scm"
    generators = "cmake"


    def build(self):
        self.run("python mk-generator.py")
        if (self.settings.os=="Linux"):
            if (self.settings.compiler=="gcc"):
                self.run("perl build_scripts/mk.pl rebuild all gcc")
            elif (self.settings.compiler=="clang"):
                # TODO: add check on settings.compiler.libcxx value?
                self.run("perl build_scripts/mk.pl rebuild all clang -DOLF_NO_LLVM_LIBCXX=OFF")
            else:
                return -1
        else:
            # On windows (currently) we have only clang
            self.run("perl build_scripts/mk.pl rebuild all clang")
