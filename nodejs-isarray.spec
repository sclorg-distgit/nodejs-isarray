# spec file for package nodejs-nodejs-isarray
%{?scl:%scl_package nodejs-nodejs-isarray}
%{!?scl:%global pkg_name %{name}}

%global npm_name isarray
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-isarray
Version:	0.0.1
Release:	5%{?dist}
Summary:	Array#isArray for older browsers
Url:		https://github.com/juliangruber/isarray
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT
# License text is included in README.md file
BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
Array#isArray for older browsers

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr build/ component.json package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/isarray

%doc README.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.1-5
- rebuilt

* Sat Feb 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.1-4
- rebuilt

* Tue Sep 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.1-3
- Add build/ to %%install

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.1-2
- Initial build
