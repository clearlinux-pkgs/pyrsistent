#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyrsistent
Version  : 0.12.3
Release  : 16
URL      : http://pypi.debian.net/pyrsistent/pyrsistent-0.12.3.tar.gz
Source0  : http://pypi.debian.net/pyrsistent/pyrsistent-0.12.3.tar.gz
Summary  : Persistent/Functional/Immutable data structures
Group    : Development/Tools
License  : MIT
Requires: pyrsistent-python
Requires: six
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

%description python
python components for the pyrsistent package.


%prep
%setup -q -n pyrsistent-0.12.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496585562
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1496585562
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
