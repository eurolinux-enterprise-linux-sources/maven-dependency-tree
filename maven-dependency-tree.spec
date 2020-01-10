
Name:          maven-dependency-tree
Version:       2.0
Release:       6%{?dist}
Summary:       Maven dependency tree artifact
Group:         Development/Libraries
License:       ASL 2.0
Url:           http://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-containers-component-annotations

Provides:      maven-shared-dependency-tree = %{version}-%{release}
Obsoletes:     maven-shared-dependency-tree < %{version}-%{release}

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%package javadoc
Group:         Documentation
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_add_dep org.apache.maven:maven-compat:3.0.4
%pom_add_dep org.apache.maven:maven-artifact:2.2.1

%build
# we have no jmock yet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0-6
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-2
- Build with xmvn

* Wed Oct 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-1
- Initial package
