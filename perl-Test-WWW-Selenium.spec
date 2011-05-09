%define upstream_name    Test-WWW-Selenium
%define upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Test applications using Selenium Remote Control
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl-libwww-perl
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Mock::LWP)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(URI::Escape)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Selenium Remote Control (SRC) is a test tool that allows you to write
automated web application UI tests in any programming language against any
HTTP website using any mainstream JavaScript-enabled browser. SRC provides
a Selenium Server, which can automatically start/stop/control any supported
browser. It works by using Selenium Core, a pure-HTML+JS library that
performs automated tasks in JavaScript; the Selenium Server communicates
directly with the browser using AJAX (XmlHttpRequest).

http://www.openqa.org/selenium-rc/

This module sends commands directly to the Server using simple HTTP
GET/POST requests. Using this module together with the Selenium Server, you
can automatically control any supported browser.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


