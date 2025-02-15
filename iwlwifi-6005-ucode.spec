%define name iwlwifi-6005-ucode
%define tarname iwlwifi-6000g2a-ucode
%define version 18.168.6.1
%define release 2

Summary: Intel PRO/Wireless 6005AGN microcode
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/%{tarname}-%{version}.tgz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 https://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-6000g2a-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 6005AGN Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%files
%doc LICENSE.* README.*
/lib/firmware/*.ucode
