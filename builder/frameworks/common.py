'''
   Copyright 2023 (c) WizIO ( Georgi Angelov )
'''

from os import listdir
from os.path import join, exists
from SCons.Script import Builder

def dev_create_template(env, template=None):
    dir = join( env.subst('$PROJECT_DIR'), 'src' )
    if not listdir( dir ):
        if template:
            template(env)
        else:
            open( join( dir, 'main.c' ), 'w').write('''//  Copyright 2023 (c) WizIO ( Georgi Angelov
#include <stdint.h>

int main(void) {
    while(1)
        continue;
}

void __attribute__((weak)) _init(){}
''')

    file = join( env.subst('$PROJECT_DIR'), 'SConscript' )
    if not exists( file ):
        open( file, 'w').write("""# Copyright 2023 (c) WizIO ( Georgi Angelov )

from os.path import join
Import('env')

env.Append(
    CPPDEFINES      = [  ],
    CPPPATH         = [  ],
    CFLAGS          = [  ],
    CCFLAGS         = [  ],
    CXXFLAGS        = [  ],
    LINKFLAGS       = [  ],
    LIBS            = [  ],
    LIBSOURCE_DIRS  = [  ],
    LIBPATH         = [  ],
    LDSCRIPT_PATH   = '',
)

# env.BuildSources( 'dst', 'src', 'filter' )

# env.BoardConfig().update('upload.maximum_ram_size',  40960) # optional
# env.BoardConfig().update('upload.maximum_size',     262144) # optional
""")

def dev_init(env):
    env.Append(
        ASFLAGS = [ env.cortex,
            '-x', 'assembler-with-cpp'
        ],
        CPPPATH = [
            join('$PROJECT_DIR', 'src'),
            join('$PROJECT_DIR', 'lib'),
            join('$PROJECT_DIR', 'include'),
        ],
        CCFLAGS = [ env.cortex, '-Os',
            '-fdata-sections',
            '-ffunction-sections',
            '-Wall',
            '-Wextra',
            '-Wfatal-errors',
            '-Wno-unused-parameter',
            '-Wno-unused-function',
            '-Wno-unused-variable',
            '-Wno-unused-value',
        ],
        CXXFLAGS = [
            '-fno-rtti',
            '-fno-exceptions',
            '-fno-threadsafe-statics',
            '-fno-non-call-exceptions',
            '-fno-use-cxa-atexit',
        ],
        LIBS = ['c', 'm'],
        LINKFLAGS = [ env.cortex, '-Os',
            '-nostartfiles',
            '-Wl,--gc-sections,--relax',
            '-Wl,-Map=%s.map' % env.subst( join('$BUILD_DIR','$PROGNAME') ),
        ],
        LIBPATH = [
            join('$PROJECT_DIR', 'lib'),
        ],
        LIBSOURCE_DIRS = [
            join('$PROJECT_DIR', 'lib'),
        ],
        BUILDERS = dict(
            ELF2HEX = Builder(
                action = env.VerboseAction(' '.join([ '$OBJCOPY', '-O',  'ihex', '$SOURCES', '$TARGET', ]), 'Building HEX $TARGET'),
                suffix = '.hex'
            ),
            ELF2BIN = Builder(
                action = env.VerboseAction(' '.join([ '$OBJCOPY', '-O',  'binary', '-S', '$SOURCES', '$TARGET', ]), 'Building BIN $TARGET'),
                suffix = '.bin'
            ),
        ),
    )
