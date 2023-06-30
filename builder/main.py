'''
   Copyright 2023 (c) WizIO ( Georgi Angelov )
'''

from os.path import join, dirname
from SCons.Script import (AlwaysBuild, Default, DefaultEnvironment)

env = DefaultEnvironment()

print( '\n<<< ARM EXPERIMENTAL PLATFORM(IO) 2023 Georgi Angelov >>>\n' )
env['PLATFORM_DIR' ] = env.platform_dir  = dirname( env['PLATFORM_MANIFEST'] )
env['FRAMEWORK_DIR'] = env.framework_dir = env.PioPlatform().get_package_dir( 'framework-wizio-arm' )
env.Replace(
    BUILD_DIR = env.subst('$BUILD_DIR'),
    ARFLAGS = ['rc'],
    AR = 'arm-none-eabi-ar',
    AS = 'arm-none-eabi-as',
    CC = 'arm-none-eabi-gcc',
    GDB = 'arm-none-eabi-gdb',
    CXX = 'arm-none-eabi-g++',
    OBJCOPY = 'arm-none-eabi-objcopy',
    RANLIB = 'arm-none-eabi-ranlib',
    SIZETOOL = 'arm-none-eabi-size',
    SIZEPROGREGEXP = r"^(?:\.boot2|\.text|\.data|\.rodata|\.text.align|\.ARM.exidx)\s+(\d+).*",
    SIZEDATAREGEXP = r'^(?:\.data|\.bss|\.ram_vector_table)\s+(\d+).*',
    SIZECHECKCMD = '$SIZETOOL -A -d $SOURCES',
    #SIZEPRINTCMD = '$SIZETOOL --mcu=arm -C -d $SOURCES', # TODO check?
    PROGSUFFIX = '.elf',
)

elf = env.BuildProgram()
bin = env.ELF2BIN( join('$BUILD_DIR', '${PROGNAME}'), elf )
hex = env.ELF2HEX( join('$BUILD_DIR', '${PROGNAME}'), elf )
prg = env.Alias( 'buildprog', hex)
AlwaysBuild( hex, bin )
Default( hex, bin )
