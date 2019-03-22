# Created by pyp2rpm-3.3.2
%global pypi_name radon

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Code Metrics in Python

License:        MIT
URL:            https://radon.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(colorama) < 0.5
BuildRequires:  python3dist(colorama) >= 0.4
BuildRequires:  python3dist(flake8-polyfill)
BuildRequires:  python3dist(mando) < 0.7
BuildRequires:  python3dist(mando) >= 0.6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(sphinx)

%description
 .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(colorama) < 0.5
Requires:       python3dist(colorama) >= 0.4
Requires:       python3dist(flake8-polyfill)
Requires:       python3dist(mando) < 0.7
Requires:       python3dist(mando) >= 0.6
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 .. image::

%package -n python-%{pypi_name}-doc
Summary:        radon documentation
%description -n python-%{pypi_name}-doc
Documentation for radon

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# There are tests it seems, but `setup.py test` is not a valid subcommand.
#%%check
#%%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/radon
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 3.0.1-1
- Initial package.
