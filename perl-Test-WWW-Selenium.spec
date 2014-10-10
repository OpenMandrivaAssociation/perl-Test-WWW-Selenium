%define upstream_name    Test-WWW-Selenium
%define upstream_version 1.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Test applications using Selenium Remote Control
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-WWW-Selenium-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Mock::LWP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(URI::Escape)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 672878
- update to new version 1.25

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.240.0-2
+ Revision: 657849
- rebuild for updated spec-helper

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.240.0-1
+ Revision: 636803
- update to new version 1.24

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.230.0-2mdv2011.0
+ Revision: 624834
- Add libwww-perl to the dependencies explicitly
- import perl-Test-WWW-Selenium



