%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

Name:               python%{python3_pkgversion}-iniconfig
Version:            1.1.1
Release:            2%{?dist}
Summary:            Brain-dead simple parsing of ini files
License:            MIT
URL:                http://github.com/RonnyPfannschmidt/iniconfig
BuildArch:          noarch
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-rpm-macros
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-wheel

Source0:            %{pypi_source iniconfig}

# pytest 6+ needs this and this uses pytest for tests
%bcond_without tests

%if %{with tests}
BuildRequires:      python%{python3_pkgversion}-pytest
%endif

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%prep
%autosetup -n iniconfig-%{version}
# Remove undeclared dependency on python-py
# Merged upstream https://github.com/pytest-dev/iniconfig/pull/47
sed -i "s/py\.test/pytest/" testing/test_iniconfig.py


# Remove dependency on setuptools-scm
sed -i "s/ *use_scm_version=.*,/version='%{version}',/" setup.py


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-iniconfig
%doc README.txt
%license LICENSE
%{python3_sitelib}/iniconfig-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/iniconfig/


%changelog
* Wed Feb 01 2023 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-2
- Enable tests

* Fri Dec 02 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-1
- Initial package
- Fedora contributions by:
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Tomas Hrnciar <thrnciar@redhat.com>
