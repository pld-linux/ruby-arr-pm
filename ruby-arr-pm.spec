#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	arr-pm
Summary:	RPM reader and writer library
Name:		ruby-%{pkgname}
Version:	0.0.10
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	6c23ba073b590440c37042a85e0786d3
URL:		https://github.com/jordansissel/ruby-arr-pm
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-flores
%endif
Requires:	cpio
Requires:	ruby-cabin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows to you to read and write rpm packages. Written in
pure ruby because librpm is not available on all systems

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
