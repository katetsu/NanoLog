from conans import ConanFile, CMake, tools


class NanoLogConan(ConanFile):
    name = "NanoLog"
    version = "0.91"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/katetsu/NanoLog.git")
        self.run("cd NanoLog")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="NanoLog")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="NanoLog")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["NanoLog"]

