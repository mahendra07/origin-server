%global cartridgedir %{_libexecdir}/openshift/cartridges/cron

Summary:       Embedded cron support for OpenShift
Name:          openshift-origin-cartridge-cron
Version: 1.18.2
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

Obsoletes: openshift-origin-cartridge-cron-1.4

BuildArch:     noarch

%description
Cron cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Feb 10 2014 Adam Miller <admiller@redhat.com> 1.18.2-1
- Cleaning specs (dmcphers@redhat.com)
- Increase cron max run time (dmcphers@redhat.com)

* Thu Jan 30 2014 Adam Miller <admiller@redhat.com> 1.18.1-1
- bump_minor_versions for sprint 40 (admiller@redhat.com)

* Thu Jan 23 2014 Adam Miller <admiller@redhat.com> 1.17.3-1
- Merge pull request #4558 from bparees/latest_versions
  (dmcphers+openshiftbot@redhat.com)
- Bump up cartridge versions (bparees@redhat.com)

