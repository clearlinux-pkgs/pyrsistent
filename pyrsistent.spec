#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyrsistent
Version  : 0.11.13
Release  : 10
URL      : https://pypi.python.org/packages/source/p/pyrsistent/pyrsistent-0.11.13.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyrsistent/pyrsistent-0.11.13.tar.gz
Summary  : Persistent/Functional/Immutable data structures
Group    : Development/Tools
License  : MIT
Requires: pyrsistent-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
Patch1: 0001-tests.patch

%description
Pyrsistent
==========
.. image:: https://travis-ci.org/tobgu/pyrsistent.png?branch=master
:target: https://travis-ci.org/tobgu/pyrsistent

%package python
Summary: python components for the pyrsistent package.
Group: Default
Requires: six-python

%description python
python components for the pyrsistent package.


%prep
%setup -q -n pyrsistent-0.11.13
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
