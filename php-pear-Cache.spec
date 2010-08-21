%include	/usr/lib/rpm/macros.php
%define		_class		Cache
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Framework for caching of arbitrary data
Summary(pl.UTF-8):	%{_pearname} - Klasa do buforowania danych
Name:		php-pear-%{_pearname}
Version:	1.5.5
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b3d5cd9953ce666884246a1942fe0f1e
URL:		http://pear.php.net/package/Cache/
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-21
Requires:	php-pear-PEAR-core >= 1:1.7.0
Suggests:	php-pear-HTTP_Request
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(HTTP/Request.*)

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Używając klasy PEAR Cache można buforować rezultaty wywołań funkcji, a
także wyniki wyjścia całych skryptów oraz danych dzielonych pomiędzy
aplikacjami.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container

%{php_pear_dir}/data/%{_class}
