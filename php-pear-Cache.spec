%include	/usr/lib/rpm/macros.php
%define		_class		Cache
%define		_pearname	%{_class}
Summary:	%{_class} - Framework for caching of arbitrary data
Summary(pl):	%{_class} - Klasa do buforowania danych
Name:		php-pear-%{_pearname}
Version:	1.5.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

%description -l pl
U¿ywaj±c klasy PEAR Cache mo¿na buforowaæ rezultaty wywo³añ funkcji, a
tak¿e wyniki wyj¶cia ca³ych skryptów oraz danych dzielonych pomiêdzy
aplikacjami.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

install %{_pearname}-%{version}/%{_class}.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

rm $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_class}.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Container
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Container/*.php
