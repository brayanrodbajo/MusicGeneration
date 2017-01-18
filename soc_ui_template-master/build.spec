
%define debug_package %{nil}
AutoReq: 0
Name: %{_NAME}
Version: %{_version}
Release: %{_release}
Summary: soc_ui_template
Prefix:  %{_LOCATION}


Group: System/Tools
License: Proprietary
URL: https://algithub.pd.alertlogic.net/soc/soc_ui_template
Source0: build.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-XXXXXX)
%description
Alertlogic SOC UI TEMPLATE package

%prep
%setup -q -n rpmbuild/BUILD

%pre


%post

%install
pwd
mkdir -p %{buildroot}%{_LOCATION}
cp -aR * %{buildroot}%{_LOCATION}

%clean
rm -rf %{buildroot}


%files
%defattr(-,soc,soc,-)
%{_LOCATION}


%changelog
