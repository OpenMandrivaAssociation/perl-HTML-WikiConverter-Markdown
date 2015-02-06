%define upstream_name    HTML-WikiConverter-Markdown
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Convert HTML to Markdown markup
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Tagset)
BuildRequires:	perl(HTML::WikiConverter)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
This module contains rules for converting HTML into Markdown markup. You
should not use this module directly; HTML::WikiConverter is the entry point
for html->wiki conversion (eg, see synopsis above). See the
HTML::WikiConverter manpage for additional usage details.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654983
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 542890
- import perl-HTML-WikiConverter-Markdown


* Thu May 06 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
