'''
   Copyright 2023 (c) WizIO ( Georgi Angelov )
'''

import click
from SCons.Script import DefaultEnvironment
from common import dev_init, dev_create_template

env = DefaultEnvironment()
dev_create_template(env)

env.cortex = env.BoardConfig().get('build.cortex', [ '-mcpu=cortex-m0plus', '-mthumb' ] )

dev_init(env)
env.SConscript( '$PROJECT_DIR/SConscript', exports='env' )

if env['LDSCRIPT_PATH'] == '':
   print();click.secho('[ WARNING ] Please, Edit Your PROJECT/SConscript\n', fg='red')