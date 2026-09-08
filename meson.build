#
# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (c) 2026 Gene C <arch@sapience.com>
#

project('nginx-passwd', ['c'],
  version: files('src/version.txt'),
  meson_version: '>=1.10.0',
  default_options: [
    'c_std=c23',
    'warning_level=3',
    'b_pie=true',
    'prefix=/usr',
    'mandir=share/man',
    ],
)

d_etc = get_option('sysconfdir')
d_lib = get_option('libdir')
d_bin = get_option('bindir')
d_man = get_option('mandir')
d_share = get_option('datadir')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
proj_root = meson.project_source_root()
py_dep = py.dependency(embed: true)

inc_dir = []
lib_sources = []

#
# top-level files
#

#
# Python submodules
#
subdir('src/nginx_passwd_mod')

#
# Deps
#

#
# Executables
#
configure_file(
  input: 'src/nginx_passwd_mod/apps/nginx-passwd.py',
  output: 'nginx-passwd',
  copy: true,
  install_dir: d_bin,
  install_mode: 'rwxr-xr-x'
)

#
# Install
#
s_etc_scripts = 'src/scripts'
s_scripts = './scripts'
s_license = 'src/data/license'
s_changelog = 'src/data/changelog'
s_docs = 'src/data/docs'
s_configs = 'configs'
manual = 'nginx-passwd.pdf'

# 
# /usr/share/nginx_passwd/docs
# 
install_data(
  [
    s_docs / manual,
  ],
  install_dir: d_share / 'nginx_passwd/docs'
)

install_subdir(
  [
    s_docs / 'html',
  ],
  install_dir: d_share / 'nginx_passwd/docs',
  strip_directory: false
)

# 
# /usr/share/nginx_passwd 
# 
install_data(
  [
    'README.rst',
    s_changelog / 'Changelog.rst',
    'packaging/PKGBUILD',
    'packaging/.nvchecker.toml',
    'packaging/Changelog',
  ],
  install_dir: d_share / 'nginx_passwd'
)

# 
# /usr/share/licenses/nginx_passwd 
# 
install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'licenses/nginx_passwd'
)

#
# tests
#
pytest = find_program('pytest')
srcdir = proj_root / 'src'
testdir = srcdir / 'tests'

test_files = [
  'test_hash.py',
  ]

foreach this_test : test_files
  test(this_test,
    pytest,
    args: [testdir / this_test],
    env: {'PYTHONPATH': srcdir},
    suite: ['unit'],
    timeout: 60,
  )
endforeach

