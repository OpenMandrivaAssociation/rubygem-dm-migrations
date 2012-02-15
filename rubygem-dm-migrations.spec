# Generated from dm-migrations-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	dm-migrations

Summary:	DataMapper plugin for writing and speccing migrations
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-migrations
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
DataMapper plugin for writing and speccing migrations

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spec/example
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spec/matchers
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/adapters/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/exceptions
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/sql
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/exceptions/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/adapters/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-migrations/sql/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spec/example/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/spec/matchers/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
