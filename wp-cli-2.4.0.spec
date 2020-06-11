%define        _profile_dir  /etc/profile.d

Name:       wp-cli
Version:    2.4.0
Release:    1%{?dist}
Summary:    The command line interface for WordPress
License:    MIT
URL:        http://wp-cli.org/
Source0:    wp-cli-2.4.0.phar
Source1:    wp.1
Source2:    wp-completion.bash
BuildArch:  noarch
Requires:   php >= 5.4

%post
echo "Requires WordPress 3.7 or later. Versions older than the latest WordPress release may have degraded functionality"

%description
WP-CLI is the command-line interface for WordPress. 
You can update plugins, configure multisite installations and much more, without using a web browser.

%prep
md5=$(wget -nv -O - "https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar.md5")
wget -nv -O %{SOURCE0} "https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar"
[[ $(md5sum %{SOURCE0} | awk '{ print $1 }') != $md5 ]] && exit 1
wget -nv -O %{SOURCE2} "https://raw.githubusercontent.com/%{name}/%{name}/v%{version}/utils/wp-completion.bash"
chmod +x %{SOURCE0}
chmod +x %{SOURCE2}
{
   echo '.TH "WP" "1"'
   php %{SOURCE0} --help
} \
  | sed -e 's/\x1B\[1m/.SH /g' \
  | sed -e 's/\x1B\[0m//g' \
  | sed -e 's/^  wp$/  wp \\- The command line interface for WordPress/' \
  > %{SOURCE1}
%build

%install
mkdir -p %{buildroot}%{_bindir}
cp -a %{SOURCE0} %{buildroot}%{_bindir}/wp
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE1} %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_profile_dir}
cp -a %{SOURCE2} %{buildroot}%{_profile_dir}/%{name}.sh

%files
%attr(0755, root, root) %{_bindir}/wp
%attr(0644, root, root) %{_mandir}/man1/wp.1*
%attr(0755, root, root) %{_profile_dir}/%{name}.sh

%changelog
* Thu Jun 11 2020 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 2.4.0-1
- Updated to version 2.4.0
- Added bash completion
- Added PHP requirements

* Thu Apr 4 2019 Çağatay Emre Bilgen <cagatayemre.bilgen@ozguryazilim.com.tr> - 2.1.0-1
- Update version 2.1.0
- Add checksum validation.
- Improve man page generation.

* Fri Aug 17 2018 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 2.0.0-1
- Update version 2.0.0

* Wed Apr 18 2018 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 1.5.0-1
- Update version 1.5.0

* Tue Dec 12 2017 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 1.4.1-1
- Update version 1.4.1
- Remove php requirements.
- Update creating man page steps.
- Added output message. 

* Fri Jul 7 2017 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 1.2.1-1
- First release of the spec file
- Check the spec file with `rpmlint -i -v wp-cli-rpm.spec`
- Build the package with `rpmbuild -bb wp-cli-rpm.spec`
